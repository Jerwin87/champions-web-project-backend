from sqlalchemy.orm import Session

import models, schemas

def get_all_heroes(db: Session):
    return db.query(models.Hero).all()

def get_single_hero(db: Session, hero_id: int):
    return db.query(models.Hero).filter(models.Hero.hero_id == hero_id).first()

def get_all_games(db: Session):
    return db.query(models.Game).all()

