import random
import boto3
from flask import Flask, jsonify
from datetime import datetime, timedelta
import os

aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

app = Flask(__name__)

# Initialize a Boto3 S3 client
s3 = boto3.client('s3')

# Name of your S3 bucket and folder
bucket_name = 'poc-dma-shared-folder'
folder_name = 'Assemblies/'

def list_first_level_directories(bucket, prefix):
    """
    List the root-level directory names in an S3 bucket with a given prefix.
    """
    directories = set()
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter='/')
    for common_prefix in response.get('CommonPrefixes', []):
        # Extract the root-level directory name
        directory_name = common_prefix.get('Prefix').rstrip('/').split('/')[-1]
        directories.add(directory_name)
    return list(directories)

def get_random_assembly_name():
    assembly_dirs = list_first_level_directories(bucket_name, folder_name)
    return random.choice(assembly_dirs)

def get_random_dates():
    # Generate random start and end dates
    end_date = datetime.now()
    start_date = end_date - timedelta(days=random.randint(1, 30))  # Random days in the past
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")

@app.route('/get-starms-jobs', methods=['GET'])
def get_starms_jobs():
    assembly_name = get_random_assembly_name()
    start_date, end_date = get_random_dates()
    
    starms_jobs_info = {
        "assembly_name": assembly_name,
        "start_date": start_date,
        "end_date": end_date
    }
    
    return jsonify(starms_jobs_info)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
