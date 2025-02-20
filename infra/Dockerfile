# ✅ Amazon Linux 2 をベースにする
FROM amazonlinux:2

# 必要なツールをインストール
RUN yum install -y gcc gcc-c++ make automake autoconf libtool \
    leptonica leptonica-devel \
    pango pango-devel \
    cairo cairo-devel \
    icu libicu libicu-devel \
    zlib zlib-devel \
    wget curl unzip tar aws-cli jq

# ✅ EPEL リポジトリを有効化
RUN amazon-linux-extras enable epel
RUN yum install -y epel-release

# ✅ Tesseract のインストール
RUN yum install -y tesseract

# ✅ 日本語の言語データを追加
RUN mkdir -p /usr/share/tessdata
RUN curl -L -o /usr/share/tessdata/jpn.traineddata \
    https://github.com/tesseract-ocr/tessdata_best/raw/main/jpn.traineddata

# ✅ Lambda の作業ディレクトリ
WORKDIR /var/task

# ✅ Lambda ハンドラーのコピー（Bash スクリプト）
COPY lambda/handler.sh .

# ✅ 実行権限を付与
RUN chmod +x handler.sh

# ✅ AWS Lambda のエントリーポイントを Bash に変更
CMD ["/bin/sh", "/var/task/handler.handler"]
