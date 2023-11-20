from sqlalchemy.orm import Session

import models, schemas

def get_hero(db: Session, hero_id: int):
    return db.query(models.Hero).filter(models.Hero.hero_id == hero_id).first()

