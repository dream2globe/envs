from pyspark import SparkContext
from pyspark.sql import SparkSession

# spark = SparkSession.builder.getOrCreate()

# # dependancies
# ## hadoop-common-3.2.0.jar, hadoop-aws-3.2.0.jar, aws-java-sdk-bundle-1.11.375.jar
# def load_config(spark_context: SparkContext):
#     spark_context._jsc.hadoopConfiguration().set("fs.s3a.access.key", "SG9BK7JGV47AXSTK96Q8")
#     spark_context._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "0CMK2KZU010JStmDEbyhBoCQntnLdjA4DLJ6sXwU")
#     spark_context._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
#     spark_context._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
#     spark_context._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://192.168.0.242:80")
#     spark_context._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")
# load_config(spark.sparkContext)

spark = (
    SparkSession.builder.appName("average examples")
    # .master("k8s://http://192.168.0.100:6443")
    .config("spark.hadoop.fs.s3a.access.key", "SG9BK7JGV47AXSTK96Q8")
    .config("spark.hadoop.fs.s3a.secret.key", "0CMK2KZU010JStmDEbyhBoCQntnLdjA4DLJ6sXwU")
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
    .config("spark.hadoop.fs.s3a.path.style.access", "true")  # 필수는 아님
    .config("spark.hadoop.fs.s3a.endpoint", "http://192.168.0.240")
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
    .getOrCreate()
)

dataframe = spark.read.json("s3a://ceph-bkt-0f190768-3872-492c-a8fc-8f1519f4b3b5/order.json")
average = dataframe.agg({"amount": "avg"})
average.show()