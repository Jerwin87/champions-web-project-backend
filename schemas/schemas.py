from typing import Optional

from pydantic import BaseModel, Field

class HeroBase(BaseModel):
    pass

class Hero(HeroBase):
    hero_id: Optional[int] = Field(default=None, primary_key=True)
    hero_name: str
    alter_ego: str
    product_ref: Optional[str]

    class Config:
        from_attributes = True

class HeroReturn(HeroBase):
    hero_name: str 
    alter_ego: str 
    product_name: str

class ProductBase(BaseModel):
    pass

class Product(ProductBase):
    product_ref: str = Field(primary_key=True)
    product_name: str
    product_type: str
    collected: Optional[bool] = Field(default=False)

    class Config:
        from_attributes = True