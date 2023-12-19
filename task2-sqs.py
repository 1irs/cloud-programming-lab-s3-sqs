import boto3

# Створення клієнту к сервісу SQS.
sqs = boto3.client("sqs")

# Створення черги.
response = sqs.create_queue(QueueName="obrizan-queue")

# Показати URL черги.
queue_url = response["QueueUrl"]
print(queue_url)

# Показати перелік усіх черг.
response = sqs.list_queues()

print(response["QueueUrls"])

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageAttributes={
        "Author": {"DataType": "String", "StringValue": "Володимир Обрізан"},
    },
    MessageBody="повідомлення",
)

print(response["MessageId"])

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
print('Received and deleted message: %s' % message)

sqs.delete_queue(QueueUrl=queue_url)
