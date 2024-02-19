from fastapi import APIRouter
from fastapi import HTTPException
from models.deck import Deck
from models.folder import Folder
from models.flashcard import Flashcard
from config.database import folder_collection, deck_collection, flashcard_collection
from bson import ObjectId


router = APIRouter()


# GET Request
@router.get("/folders")
async def get_folders():
    folders = folder_collection.find()
    return [Folder(**folder) for folder in folders]


# POST Request
@router.post("/folders")
async def create_folder(folder: Folder):
    folder = folder.dict()
    folder_id = folder_collection.insert_one(folder)
    created_folder = folder_collection.find_one({"_id": folder_id.inserted_id})
    return Folder(**created_folder)