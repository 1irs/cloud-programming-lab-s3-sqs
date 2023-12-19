import boto3

s3 = boto3.client('s3')

# Треба вказати унікальне імʼя бакету
bucket_name = "obrizan-2023-12-18-2"

s3.create_bucket(
    Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": "us-west-1"}
)
