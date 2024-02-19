from pydantic import BaseModel
from .deck import Deck


class Folder(BaseModel):
    name: str
    description: str
    decks: list[Deck] = []
    color: str
    starred: bool = False
    public: bool = False
    owner: str
    collaborators: list[str] = []
    created_at: str
    updated_at: str
    deleted_at: str
    deleted: bool = False