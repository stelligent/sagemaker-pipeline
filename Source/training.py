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
