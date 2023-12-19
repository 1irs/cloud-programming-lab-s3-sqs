import boto3

# Створення клієнту к сервісу SQS.
sqs = boto3.client("sqs")

# Створення черги.
response = sqs.create_queue(QueueName="obrizan-queue")
queue_url = response["QueueUrl"]

while True:
    print("Waiting for messages...")

    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=["SentTimestamp"],
        MaxNumberOfMessages=1,
        MessageAttributeNames=["All"],
        WaitTimeSeconds=20,
    )
    messages = response.get("Messages", [])
    if len(messages) == 0:
        continue

    for message in messages:
        print(message["MessageId"], message["Body"])
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message["ReceiptHandle"])
