from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Get dictionary from database
# def dict_factory(cursor, row):
#     fields = [column[0] for column in cursor.description]
#     return {key: value for key, value in zip(fields, row)}
# con.row_factory = dict_factory


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/heroes/{hero_id}", response_model=schemas.Hero)
def get_hero(hero_id: int, db: Session = Depends(get_db)):
    db_hero = crud.get_hero(db, hero_id=hero_id)
    if db_hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return db_hero

# @app.get("/heroes")
# async def get_heroes():
#     query = "SELECT * FROM heroes"
#     try:
#         heroes = con.execute(query).fetchall()
#     except sqlite3.OperationalError: 
#         return {"ERROR": "sqlite3.OperationalError"}
#     else:
#         return heroes

# @app.get("/aspects")
# async def get_aspects():
#     query = "SELECT * FROM aspects"
#     try:
#         aspects = con.execute(query).fetchall()
#     except sqlite3.OperationalError: 
#         return {"ERROR": "sqlite3.OperationalError"}
#     else:
#         return aspects

# @app.get("/aspects/{aspect_id}")
# async def get_aspect(aspect_id: int):
#     query = f"SELECT * FROM aspects WHERE aspect_id={aspect_id}"
#     try:
#         aspect = con.execute(query).fetchone()
#     except sqlite3.OperationalError: 
#         return {"ERROR": "sqlite3.OperationalError"}
#     else:
#         if aspect is None:
#             return {"message": "aspect not found"}
#         else:
#             return aspect

# @app.get("/products")
# async def get_products():
#     query = "SELECT * FROM products"
#     try:
#         products = con.execute(query).fetchall()
#     except sqlite3.OperationalError: 
#         return {"ERROR": "sqlite3.OperationalError"}
#     else:
#         return products

# @app.get("/products/{product_id}")
# async def get_product(product_id: int):
#     query = f"SELECT * FROM products WHERE product_id={product_id}"
#     try:
#         product = con.execute(query).fetchone()
#     except sqlite3.OperationalError: 
#         return {"ERROR": "sqlite3.OperationalError"}
#     else:
#         if product is None:
#             return {"message": "product not found"}
#         else:
#             return product

# @app.get("/encounter_sets")
# async def get_encounter_sets():
#     query = "SELECT * FROM encounter_sets"
#     try:
#         sets = con.execute(query).fetchall()
#     except sqlite3.OperationalError: 
#         return {"ERROR": "sqlite3.OperationalError"}
#     else:
#         return sets

# @app.get("/encounter_sets/{set_id}")
# async def get_aspect(set_id: int):
#     query = f"SELECT * FROM encounter_sets WHERE set_id={set_id}"
#     try:
#         set = con.execute(query).fetchone()
#     except sqlite3.OperationalError: 
#         return {"ERROR": "sqlite3.OperationalError"}
#     else:
#         if set is None:
#             return {"message": "product not found"}
#         else:
#             return set
        
# @app.get("/stats/{hero_id}")
# async def get_hero_stats(hero_id: int):#q: Annotated[list[]]):
#     query = f"SELECT * FROM heroes WHERE hero_id={hero_id}"
#     try:
#         hero = con.execute(query).fetchone()
#     except sqlite3.OperationalError: 
#         return {"ERROR": "sqlite3.OperationalError"}
#     else:
#         if hero is None:
#             return {"message": "hero not found"}
#         else:
#             return hero