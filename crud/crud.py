from sqlalchemy.orm import Session

from models.models import Hero, Product
from schemas import schemas

#create
def create_hero(db: Session, hero: schemas.Hero):
    hero = Hero(
        hero_id = hero.hero_id,
        hero_name = hero.hero_name,
        alter_ego = hero.alter_ego,
        product_ref = hero.product_ref
    )
    db.add(hero)
    db.commit()
    db.refresh(hero)
    return (hero)

def create_product(db: Session, product: schemas.Product):
    product = Product(
        product_ref = product.product_ref,
        product_name = product.product_name,
        product_type = product.product_type
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

#read
def read_all_products(db: Session):
    return db.query(Product).all()

def read_product_by_ref(db: Session, product_ref: str):
    return db.query(Product).filter(Product.product_ref == product_ref).first()

def read_all_heroes(db: Session):
    return db.query(Hero.hero_name, Hero.alter_ego, Product.product_name).join(Product).all()

def read_single_hero(db: Session, hero_id: int):
    return db.query(Hero).filter(Hero.hero_id == hero_id).first()

#def get_all_games(db: Session):
    #return db.query(Game).all()


