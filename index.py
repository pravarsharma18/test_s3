import boto3
import conf

from datetime import date, datetime

s3 = boto3.client('s3', aws_access_key_id=conf.AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=conf.AWS_SECRET_ACCESS_KEY,
                  region_name=conf.S3DIRECT_REGION)

response = s3.list_buckets()

# s3.list_objects_v2(Bucket="gready-bucket", Delimiter='/', Prefix="media/")

# with open("prefix_delimeter1.txt", "a+") as f:
#     f.write(str(s3.list_objects_v2(Bucket="gready-bucket", Delimiter='/')))

def get_all_bucket_objects(bucket_name):
    return s3.list_objects_v2(Bucket=bucket_name, Delimiter='/')

def get_all_bucket_folder(bucket_name, folder):
    return s3.list_objects_v2(Bucket=bucket_name, Delimiter='/', Prefix=folder)

def create_s3_bucket(bucket_name, location):
    configuration = {
        'LocationConstraint': location
    }
    res = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=configuration)
    return res


# s3.put_object(Bucket="pravar19921807", Key=("Goa/abc/pqr" + '/'))

# a = s3.delete_objects(Bucket="pravar19921807", Key=("Goa/"))

# bucket = s3.get_bucket("gready-bucket")
# folders = bucket.list('', '/')
# for folder in folders:
#     print(folder.name)

# print(response.get('Buckets'))
# with open('a.txt', 'a') as f:
#     # print(type(all_objects))
#     f.write(str(all_objects.get('Contents')))

# for i in all_objects.get('Contents'):
#     # print(i['Key'])
#     with open('objects.txt', 'a') as f:
#         f.write(i['Key'])
#         f.write("\n")

# print(all_objects.get('Contents'))


# https://gready-bucket.s3.amazonaws.com/media/Carousel_Images_1/home_product_bg.jpg
