from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

class HeroBase(BaseModel):
    pass

class Hero(HeroBase):
    hero_id: int
    hero_name: str
    alter_ego: str
    product_ref: str

    class Config:
        orm_mode = True

class GameBase(BaseModel):
    pass

class Game(GameBase):
    game_id: int
    date: datetime
    hero_id: int
    villain_id: int
    difficulty: str
    heroic: int
    custom: bool
    win: bool
    campaign: bool
    precon: bool
    encounter_set_ids: Optional[List[int]] = None
    encounter_set_names: Optional[List[str]] = None
    aspect_ids: Optional[List[int]] = None
    aspect_names: Optional[List[str]] = None
