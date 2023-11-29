from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base

class Hero(Base):
    __tablename__ = "heroes"

    hero_id = Column(Integer, primary_key=True, index=True)
    hero_name = Column(String)
    alter_ego = Column(String)
    product_ref = Column(String)

class Game(Base):
    __tablename__ = "games"

    game_id= Column(Integer, primary_key=True, index=True) 
    date= Column(Date)
    hero_id= Column(Integer, ForeignKey("heroes.hero_id"))
    villain_id= Column(Integer, ForeignKey("encounter_sets.set_id"))
    difficulty= Column(String)
    heroic= Column(Integer)
    custom= Column(Boolean)
    win= Column(Boolean)
    campaign= Column(Boolean)
    precon= Column(Boolean)