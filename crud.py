from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from vibeosys_assignment import models, schemas, database

from database import engine, Base, get_db

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vibeosys Product API")

@app.get("/product/list", response_model=list[schemas.ProductOut])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    skip = (page - 1) * 10
    products = crud.get_products(db, skip=skip, limit=10)
    return products

@app.get("/product/{pid}/info", response_model=schemas.ProductOut)
def get_product(pid: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/add", response_model=schemas.ProductOut)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.put("/product/{pid}/update", response_model=schemas.ProductOut)
def update_product(pid: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db, pid, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product
