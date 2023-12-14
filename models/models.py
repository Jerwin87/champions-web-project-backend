from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Relationship
from database import Base


# Main Tabel classes
class Hero(Base):
    __tablename__ = "heroes"

    hero_id = Column(Integer, primary_key=True, autoincrement=True)
    hero_name = Column(String(80), nullable=False)
    alter_ego = Column(String(80))
    product_ref = Column(String(80), ForeignKey("products.product_ref"), nullable=False, index=True)
        
    product = Relationship("Product", back_populates="heroes")

class Product(Base):
    __tablename__ = "products"

    product_ref = Column(String(80), primary_key=True, nullable=False)
    product_name = Column(String(80), nullable=False)
    product_type = Column(String(80), nullable=False)
    collected = Column(Boolean, default=False)

    heroes = Relationship("Hero", back_populates="product")