# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
#storage_client = storage.Client()
storage_client = storage.Client.from_service_account_json(r'C:\Users\Prasad Kudale\Desktop\YouTube\cloud\demo.json')

# The name for the new bucket
bucket_name = 'pashcloud0002'

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print("Bucket Created")

bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob("a1.txt")
blob.upload_from_filename("a1.txt")

print("File Uploaded")

blob = bucket.blob("a1.txt")
blob.download_to_filename("download.txt")

print("File Downloaded")