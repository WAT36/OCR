import os
import boto3
import subprocess

# S3 クライアントを初期化
s3 = boto3.client('s3')

# OCR を実行する関数
def process_image(bucket_name, object_key):
    local_file = f"/tmp/{object_key}"
    output_file = f"/tmp/{object_key}.txt"

    # S3 から画像をダウンロード
    s3.download_file(bucket_name, object_key, local_file)

    # Tesseract を実行して OCR
    subprocess.run([
        "tesseract", local_file, output_file.replace('.txt', ''),
        "-l", "jpn", "--tessdata-dir", "/usr/share/tessdata"
    ], check=True)

    # OCR 結果を S3 にアップロード
    result_key = f"results/{object_key}.txt"
    s3.upload_file(output_file, bucket_name, result_key)

    return result_key

# Lambda ハンドラー
def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        print(f"Processing {object_key} from bucket {bucket_name}")

        # OCR を実行
        result_key = process_image(bucket_name, object_key)
        print(f"OCR result saved to {result_key}")

    return {"status": "done"}
