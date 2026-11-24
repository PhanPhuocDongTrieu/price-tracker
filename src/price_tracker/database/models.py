from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    site = Column(String)
    target_price = Column(Float)
    prices = relationship("PriceHistory", back_populates="product")


class PriceHistory(Base):
    __tablename__ = "price_history"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    price = Column(Float, nullable=False)
    scraped_at = Column(DateTime, default=datetime.utcnow)
    product = relationship("Product", back_populates="prices")
