FROM spark-base/spark-py:3.1.2

USER root

# # spark jars
# ADD https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.0/hadoop-aws-3.2.0.jar /opt/spark/jars/
# ADD https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.375/aws-java-sdk-bundle-1.11.375.jar /opt/spark/jars/

# apt-get
RUN apt-get update && apt-get install -y \
    apt-utils \
    bash-completion \
    && rm -rf /var/lib/apt/lists

# pip
WORKDIR /app
ADD requirements.txt .
RUN pip3 install -r requirements.txt

# source
WORKDIR /app
ADD main.py .