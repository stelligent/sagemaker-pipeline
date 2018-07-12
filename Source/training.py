import boto3
import re
import os
import wget
import time
from time import gmtime, strftime
import sys
import json

start = time.time()

role = sys.argv[1]
bucket = sys.argv[2]
commitID = sys.argv[3]
commitID = commitID[0:7]

training_image = '811284229777.dkr.ecr.us-east-1.amazonaws.com/image-classification:latest'

def download(url):
    filename = url.split("/")[-1]
    if not os.path.exists(filename):
        wget.download(url, filename)

        
def upload_to_s3(channel, file):
    s3 = boto3.resource('s3')
    data = open(file, "rb")
    key = channel + '/' + file
    s3.Bucket(bucket).put_object(Key=key, Body=data)

# caltech-256
print ("Downloadng Training Data")
download('http://data.mxnet.io/data/caltech-256/caltech-256-60-train.rec')
upload_to_s3('train', 'caltech-256-60-train.rec')
print ("Finished Downloadng Training Data")
print ("Downloadng Testing Data")
download('http://data.mxnet.io/data/caltech-256/caltech-256-60-val.rec')
upload_to_s3('validation', 'caltech-256-60-val.rec')
print ("Finished Downloadng Testing Data")

config_data = {
  "Parameters":
    {
      "BucketName": bucket,
      "CommitID": commitID,
      "SageMakerRole": role
    }
}

json_config_data = json.dumps(config_data)

f = open( './CloudFormation/configuration.json', 'w' )
f.write(json_config_data)
f.close()

end = time.time()
print(end - start)
