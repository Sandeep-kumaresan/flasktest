from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client.get_database("testdb")
collection = db.get_collection("items")

@app.route('/')
def home():
    return "Flask App running successfully!"

@app.route('/items', methods=['GET'])
def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Item added!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
