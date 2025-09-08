from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from vibeosys_assignment import models, schemas, database

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# List products with pagination
@app.get("/product/list", response_model=List[schemas.ProductOut])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    limit = 10
    offset = (page - 1) * limit
    products = db.query(models.Product).offset(offset).limit(limit).all()
    return products


# Get product by ID
@app.get("/product/{pid}/info", response_model=schemas.ProductOut)
def get_product(pid: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.product_id == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Add product
@app.post("/product/add", response_model=schemas.ProductOut)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


# Update product
@app.put("/product/{pid}/update", response_model=schemas.ProductOut)
def update_product(pid: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.product_id == pid).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product.dict().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product
