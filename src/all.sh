#!/bin/bash

# 引数の数が２つかチェックする
if [ "$#" -ne 2 ]; then
  echo "Error: Usage $0 (Input img file) (Output formatted csv file)"
  exit 1
fi

INPUT_IMG_FILE=$1
OUTPUT_CSV_FILE=$2
INPUT_IMG_NAME=${INPUT_IMG_FILE/%.PNG/}

# ファイル存在チェック
if [ ! -f $INPUT_IMG_FILE ]; then
    echo "Error: $INPUT_IMG_FILE is not found!!"
    exit 1
fi

PWD=`pwd`
DIR=`dirname $0`
cd $DIR

# 入力画像を左右半分に分ける
python3 trimmer.py $INPUT_IMG_FILE
rc=$?
if [ $rc -ne 0 ]; then
  echo "Error occured in trimmer.py"
  cd $PWD
  exit 1
fi
echo "--- Success - trimmer ---"

INPUT_IMG_LEFT_NAME="${INPUT_IMG_NAME}-left"
INPUT_IMG_RIGHT_NAME="${INPUT_IMG_NAME}-right"
DATE=`date +%Y%m%d%H%M%S`
OUTPUT_LEFT_TXT="./output/${DATE}-left"
OUTPUT_RIGHT_TXT="./output/${DATE}-right"


# 画像を文字起こしする
./tesseract.sh "${INPUT_IMG_LEFT_NAME}.png" ${OUTPUT_LEFT_TXT}
rc=$?
if [ $rc -ne 0 ]; then
  echo "Error occured in tesseract left"
  cd $PWD
  exit 1
fi
echo "--- Success - tesseract left ---"

./tesseract.sh "${INPUT_IMG_RIGHT_NAME}.png" ${OUTPUT_RIGHT_TXT}
rc=$?
if [ $rc -ne 0 ]; then
  echo "Error occured in tesseract right"
  cd $PWD
  exit 1
fi
echo "--- Success - tesseract right ---"

# 文字起こしデータをcsvに変換する
python3 csv_adapter.py "${OUTPUT_LEFT_TXT}.txt" "${OUTPUT_RIGHT_TXT}.txt" ${OUTPUT_CSV_FILE}
rc=$?
if [ $rc -ne 0 ]; then
  echo "Error occured in csv_adapter"
  cd $PWD
  exit 1
fi
echo "--- Success - csv_adapter ---"

# この後　答えの更新は自分の手でやること