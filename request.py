import boto3
import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth
from PIL import Image
import io
import conf


def get_image_url(bucket, endpoint):
    auth = AWSRequestsAuth(aws_access_key=conf.AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=conf.AWS_SECRET_ACCESS_KEY,
                           aws_host=f'{bucket}.s3.amazonaws.com',
                           aws_region='us-east-1',
                           aws_service='s3'
                           )
    r = requests.get(f"https://{bucket}.s3.amazonaws.com/{endpoint}", auth=auth)
    return r.url

    # image = Image.open(io.BytesIO(r.content))
    # image = image.convert('RGB')
    # image.save("avatar-icon.jpg")
    # image.save("avatar-icon.jpg")
    # print(r)
