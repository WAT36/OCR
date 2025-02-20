#!/bin/bash

echo "starting Lambda Function"

# 環境変数から S3 バケット名を取得
BUCKET_NAME="ocr-cdk"

# Lambda の標準入力からイベントデータを取得
EVENT_DATA=$(cat -)

# S3 のオブジェクトキーを jq で取得
OBJECT_KEY=$(echo "$EVENT_DATA" | jq -r '.Records[0].s3.object.key')

echo "BUCKET_NAME: $BUCKET_NAME"
echo "EVENT_DATA: $EVENT_DATA"
echo "OBJECT_KEY: $OBJECT_KEY"
echo $#

if [ -z "$BUCKET_NAME" ] || [ -z "$OBJECT_KEY" ]; then
    echo "Error: BUCKET_NAME or OBJECT_KEY is not set."
    exit 1
fi

LOCAL_FILE="/tmp/$(basename "$OBJECT_KEY")"
OUTPUT_FILE="/tmp/$(basename "$OBJECT_KEY").txt"

echo "Downloading S3 object: s3://$BUCKET_NAME/$OBJECT_KEY"
aws s3 cp "s3://$BUCKET_NAME/$OBJECT_KEY" "$LOCAL_FILE"

if [ ! -f "$LOCAL_FILE" ]; then
    echo "Error: File download failed"
    exit 1
fi

echo "Running Tesseract OCR..."
tesseract "$LOCAL_FILE" "${OUTPUT_FILE%.txt}" -l jpn --tessdata-dir /usr/share/tessdata

if [ ! -f "$OUTPUT_FILE" ]; then
    echo "Error: Tesseract OCR failed"
    exit 1
fi

RESULT_KEY="output/$(basename "$OBJECT_KEY").txt"

echo "Uploading OCR result to S3..."
aws s3 cp "$OUTPUT_FILE" "s3://$BUCKET_NAME/$RESULT_KEY"

echo "OCR result uploaded: s3://$BUCKET_NAME/$RESULT_KEY"

exit 0
