import boto3
import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth
from PIL import Image
import io
import conf

auth = AWSRequestsAuth(aws_access_key=conf.AWS_ACCESS_KEY_ID,
                       aws_secret_access_key=conf.AWS_SECRET_ACCESS_KEY,
                       aws_host='gready-bucket.s3.amazonaws.com',
                       aws_region='us-east-1',
                       aws_service='s3')

r = requests.get("https://gready-bucket.s3.amazonaws.com/media/avatar-icon.jpg", auth=auth)

# print(r.content)

image = Image.open(io.BytesIO(r.content))
image = image.convert('RGB')
image.save("avatar-icon.jpg")
# image.save("avatar-icon.jpg")
# print(r)
