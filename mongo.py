from pymongo import MongoClient
from faker import Faker
import random


# Initialize the Faker library

fake = Faker()
URI = 'mongodb+srv://vishvaahacker:qte7tT6FAUTTxsUR@cluster0.5h9tr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
range_to = int(input("Enter Data Count : "))


# Connect to MongoDB

client = MongoClient('localhost', 27017)
db = client['TestData']
collection = db['Data']

# Generate 1000 records
data = []
for e in range(range_to):
    record = {
        "name": fake.name(),
        "age": random.randint(18, 80),
        "number": fake.numerify('+91 ##########'),
        "job": fake.job(),
        "hobbies": fake.words(nb=3)  # Generates a list of 3 random words
    }
    data.append(record)
    print(e)

# Insert data into MongoDB
collection.insert_many(data)


# Close the connection
client.close()

print("records inserted successfully.")
print(f"{range_to} records inserted")





