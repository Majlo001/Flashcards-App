from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")

client = MongoClient(f"mongodb+srv://{mongo_user}:{mongo_password}@cluster0.qwhjf8u.mongodb.net/?retryWrites=true&w=majority")

db = client.flashcards_db
folder_collection = db["folder_collection"]
deck_collection = db["deck_collection"]
flashcard_collection = db["flashcard_collection"]
