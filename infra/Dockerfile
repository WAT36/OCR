# ✅ AWS Lambda の Python 3.8 公式イメージを使用
FROM public.ecr.aws/lambda/python:3.8

# 必要なツールをインストール
RUN yum install -y gcc gcc-c++ make automake autoconf libtool \
    leptonica leptonica-devel \
    pango pango-devel \
    cairo cairo-devel \
    icu libicu libicu-devel \
    zlib zlib-devel \
    wget curl unzip tar

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

# ✅ Python パッケージをインストール
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ✅ Lambda ハンドラーのコピー
COPY lambda/app.py .

# ✅ AWS Lambda のエントリーポイント
CMD ["app.lambda_handler"]
