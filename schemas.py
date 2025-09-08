from pydantic import BaseModel
from typing import Optional
from enum import Enum


class CategoryEnum(str, Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"


class UnitEnum(str, Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"


# Base Schema (common fields)
class ProductBase(BaseModel):
    name: str
    category: CategoryEnum
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: str
    unit_of_measure: UnitEnum
    lead_time: Optional[int] = None


# Create Product
class ProductCreate(ProductBase):
    pass


# Update Product
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[CategoryEnum] = None
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: Optional[str] = None
    unit_of_measure: Optional[UnitEnum] = None
    lead_time: Optional[int] = None


# Response Schema
class ProductOut(ProductBase):
    product_id: int

    class Config:
        orm_mode = True
