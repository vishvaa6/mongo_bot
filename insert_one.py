from pymongo import MongoClient
from faker import Faker
import random


# Initialize the Faker library
fake = Faker()

range_to = 1000

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['TestData']
collection = db['Data']

# Generate 1000 records

record = {
    "name": fake.name(),
    "age": random.randint(18, 80),
    "number": fake.numerify('+91 ##########'),
    "job": fake.job(),
    "hobbies": fake.words(nb=1)  # Generates a list of 3 random words
    }
    
    

# Insert data into MongoDB
collection.insert_one(record)


# Close the connection
client.close()

print("records inserted successfully.")

