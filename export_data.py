import csv
from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb+srv://Database:Starboy%4025@cluster0.vkyiq.mongodb.net/")
db = client["survey_database"]  
collection = db["responses"]  

# fetch all data
data = list(collection.find({}, {"_id": 0}))

csv_file = 'survey_data,csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"Data successfully exported to {csv_file}")
