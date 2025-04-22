FROM python:3.9-slim
# 作業ディレクトリを設定
WORKDIR /app/src/

# requirements.txt をコピーして依存関係をインストール
COPY ./requirements.txt /app/src/
RUN pip install -r requirements.txt

# コンテナを終了させないためのエントリーポイント
ENTRYPOINT ["tail", "-f", "/dev/null"]
