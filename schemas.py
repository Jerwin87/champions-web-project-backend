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