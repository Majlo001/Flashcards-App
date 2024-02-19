from pydantic import BaseModel


class Flashcard(BaseModel):
    word: str
    definition: str
    starred: bool = False
