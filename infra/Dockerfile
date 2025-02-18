# AWS Lambda の Amazon Linux 2 ベースイメージ（Python 3.8）
FROM amazonlinux:2

# 必要なツールをインストール
RUN yum install -y gcc gcc-c++ make automake autoconf libtool \
    leptonica leptonica-devel \
    pango pango-devel \
    cairo cairo-devel \
    icu libicu libicu-devel \
    zlib zlib-devel \
    wget curl unzip tar python3 python3-pip

# ✅ EPEL リポジトリを有効化（最初に `amazon-linux-extras enable` を実行）
RUN amazon-linux-extras enable epel
RUN yum install -y epel-release

# Tesseract のインストール
RUN yum install -y tesseract

# 日本語の言語データを追加
RUN mkdir -p /usr/share/tessdata
RUN curl -L -o /usr/share/tessdata/jpn.traineddata \
    https://github.com/tesseract-ocr/tessdata_best/raw/main/jpn.traineddata

# Lambda の作業ディレクトリ
WORKDIR /var/task

# 必要な Python パッケージをインストール
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Lambda ハンドラーのコピー
COPY lambda/app.py .

# AWS Lambda のエントリーポイント
CMD ["app.lambda_handler"]
