from pymongo import MongoClient
from model import *

client = MongoClient("mongodb+srv://test:1234@cluster0.dxqjf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["VehicleAllocationSystem"]

#creating two collections in the database
vehicles = db['vehicles']
allocations = db['allocations']





