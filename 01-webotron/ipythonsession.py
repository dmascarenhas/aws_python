# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket)

for bucket in s3.buckets.all():
    print(bucket)
#command below errored as my profile is in us-east-1 and I don;t nneed to set LocationConstraint    
new_bucket = s3.create_bucket(Bucket='automatingawsduff-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='automatingawsduff-boto3')
for bucket in s3.buckets.all():
    print(bucket)

get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipythonsession.py 1-11')
