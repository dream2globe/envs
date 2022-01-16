FROM python:3.8

USER root

ENV AWS_ACCESS_KEY_ID=http://192.168.0.240
ENV AWS_SECRET_ACCESS_KEY=0CMK2KZU010JStmDEbyhBoCQntnLdjA4DLJ6sXwU
ENV MLFLOW_S3_ENDPOINT_URL=http://192.168.0.240
ENV MLFLOW_S3_IGNORE_TLS=false

COPY requirements.txt /root/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip --no-cache-dir install -r /root/requirements.txt

ENTRYPOINT ["mlflow", "server", "--backend-store-uri", "mysql+pymysql://mlflow:mlflow@192.168.0.241:3306/mlflow", "--default-artifact-root", "s3:/ceph-bkt-0f190768-3872-492c-a8fc-8f1519f4b3b5/mlflow", "--host", "0.0.0.0"]
EXPOSE 5000
