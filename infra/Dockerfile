# AWS Lambda の Amazon Linux 2 ベースイメージ（Python 3.8）
FROM amazonlinux:2

# 必要なツールをインストール
RUN yum install -y gcc gcc-c++ make automake autoconf libtool \
    leptonica leptonica-devel \
    pango pango-devel \
    cairo cairo-devel \
    icu libicu libicu-devel \
    zlib zlib-devel \
    wget curl unzip tar 

# ✅ `amazon-linux-extras` で Python 3.8 を有効化 & インストール
RUN amazon-linux-extras enable python3.8 \
    && yum install -y python3.8 python3.8-pip

# ✅ Python3.8 をデフォルトに設定（非対話モード）
RUN alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 \
    && alternatives --set python3 /usr/bin/python3.8

# ✅ シェルの `hash` をクリアし、`python3` コマンドを有効にする
RUN hash -r

# ✅ `python3` が正しく動作するかチェック
RUN python3 --version

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
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Lambda ハンドラーのコピー
COPY lambda/app.py .

# ✅ Lambda Entrypoint を修正（Python を直接実行するように変更）
CMD ["python3", "app.py"]

