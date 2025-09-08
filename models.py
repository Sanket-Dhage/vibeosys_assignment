from sqlalchemy import Column, Integer, String, Enum, Text, TIMESTAMP, func, BigInteger
from vibeosys_assignment.database import Base
import enum


class CategoryEnum(str, enum.Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"


class UnitEnum(str, enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"


class Product(Base):
    __tablename__ = "products"

    product_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    description = Column(String(250))
    product_image = Column(Text)
    sku = Column(String(100), unique=True, nullable=False)
    unit_of_measure = Column(Enum(UnitEnum), nullable=False)
    lead_time = Column(Integer)
    created_date = Column(TIMESTAMP, server_default=func.now())
    updated_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
