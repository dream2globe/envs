export AWS_ACCESS_KEY_ID="SG9BK7JGV47AXSTK96Q8"
export AWS_SECRET_ACCESS_KEY="0CMK2KZU010JStmDEbyhBoCQntnLdjA4DLJ6sXwU"
export MLFLOW_S3_ENDPOINT_URL="http://192.168.0.240"
export MLFLOW_S3_IGNORE_TLS="false"

mlflow server --backend-store-uri mysql+pymysql://mlflow:mlflow@192.168.0.241:3306/mlflow --default-artifact-root s3:/ceph-bkt-0f190768-3872-492c-a8fc-8f1519f4b3b5/mlflow  --host 0.0.0.0
