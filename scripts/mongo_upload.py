import pandas as pd
from pymongo import MongoClient
import sys

# 1. Setup Connection Details
# Replace <password> with your actual password and paste your connection string from Atlas
CONNECTION_STRING = "mongodb://criceco_admin:Criceco1234@ac-fpi3oqy-shard-00-00.vqj3q6a.mongodb.net:27017,ac-fpi3oqy-shard-00-01.vqj3q6a.mongodb.net:27017,ac-fpi3oqy-shard-00-02.vqj3q6a.mongodb.net:27017/?ssl=true&replicaSet=atlas-oqpfy0-shard-0&authSource=admin&appName=CricecoCluster"
DATABASE_NAME = "SecureSeat"
COLLECTION_NAME = "tickets"

try:
    # 2. Connect to MongoDB Atlas
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # 3. Read the CSV file
    # Use pandas to handle the CSV structure easily
    df = pd.read_csv('../data/tickets_rows.csv')

    # Optional: Data Cleaning/Conversion
    # For example, converting 'id' to an actual integer if it isn't already
    # df['id'] = df['id'].astype(int)

    # 4. Convert DataFrame to a list of dictionaries (JSON-like format)
    data_to_upload = df.to_dict(orient='records')

    # 5. Insert into MongoDB
    print(f"Attempting to upload {len(data_to_upload)} documents...")
    result = collection.insert_many(data_to_upload)
    
    print(f"Success! Inserted IDs: {len(result.inserted_ids)}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    client.close()
