# backend/app/models.py
from pydantic import BaseModel

class Game(BaseModel):
    id: str
    moves: list[str]

class Evaluation(BaseModel):
    fen: str
    depth: int
    evaluation: dict
