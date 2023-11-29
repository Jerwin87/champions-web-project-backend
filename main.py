from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessioLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessioLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/heroes", response_model=list[schemas.Hero])
def read_heroes(db: Session = Depends(get_db)):
    heroes = crud.get_all_heroes(db)
    return heroes
    
@app.get("/heroes/{hero_id}", response_model=schemas.Hero)
def read_hero(hero_id: int, db: Session = Depends(get_db)):
    hero = crud.get_single_hero(db, hero_id=hero_id)
    if hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

@app.get("/games", response_model=list[schemas.Game])
def read_all_games(db: Session = Depends(get_db)):
    games = crud.get_all_games(db)
    return games
    


    