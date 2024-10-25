#!/bin/bash

# 引数の数が２つかチェックする
if [ "$#" -ne 2 ]; then
  echo "Error: Usage $0 (Input img file) (Output file (no need .txt))"
  exit 1
fi

INPUT_IMG_FILE=$1
OUTPUT_FILE=$2

# ファイル存在チェック
if [ ! -f $INPUT_IMG_FILE ]; then
    echo "Error: $INPUT_IMG_FILE is not found!!"
    exit 1
fi

# 実行
tesseract $INPUT_IMG_FILE $OUTPUT_FILE -l jpn

exit 0