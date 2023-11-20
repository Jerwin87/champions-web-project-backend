from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Hero(Base):
    __tablename__ = "heroes"

    hero_id = Column(Integer, primary_key=True, index=True)
    hero_name = Column(String)
    alter_ego = Column(String)
    product_ref = Column(String)
    