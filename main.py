from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import crud.crud as crud, schemas.schemas as schemas, models.models as models
from database import SessioLocal, engine

models.Base.metadata.create_all(engine)

app = FastAPI()

# CORS
origins = ["http://localhost:3000"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

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

#heroes
@app.post("/heroes", response_model=schemas.Hero)
def post_hero(hero: schemas.Hero, db: Session = Depends(get_db)):
    #TODO: Check if Hero already in db
    return crud.create_hero(db=db, hero=hero)

@app.get("/heroes", response_model=list[schemas.HeroReturn])
def get_heroes(db: Session = Depends(get_db)):
    heroes = crud.read_all_heroes(db)
    return heroes

@app.get("/heroes/{hero_id}", response_model=schemas.Hero)
def get_hero(hero_id: int, db: Session = Depends(get_db)):
    hero = crud.read_single_hero(db, hero_id=hero_id)
    if hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

#products
@app.post("/products", response_model=schemas.Product)
def post_product(product: schemas.Product, db: Session = Depends(get_db)):
    checked_product = crud.read_product_by_ref(db=db, product_ref=product.product_ref)
    if checked_product:
        raise HTTPException(status_code=400, detail="Product already in Database")
    return crud.create_product(db=db, product=product)

@app.get("/products", response_model=list[schemas.Product])
def get_all_products(db: Session = Depends(get_db)):
    products = crud.read_all_products(db)
    return products

# @app.get("/games", response_model=list[schemas.Game])
# def read_all_games(db: Session = Depends(get_db)):
#     games = heroes.get_all_games(db)
#     return games
    


    