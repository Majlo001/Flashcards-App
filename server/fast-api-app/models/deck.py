from pydantic import BaseModel
from .flashcard import Flashcard


class Language(BaseModel):
    name: str
    icon: str


class Deck(BaseModel):
    name: str
    definition: str
    flashcards: list[Flashcard] = []
    word_language: Language
    definition_language: Language