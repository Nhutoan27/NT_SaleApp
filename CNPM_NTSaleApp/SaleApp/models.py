import json

from sqlalchemy import Column, String , Integer,Float, ForeignKey
from sqlalchemy.orm import relationship
from SaleApp import db, app

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable = False, unique=True)

class Category(Base):
    products = relationship("Product", backref="category" , lazy =True)

class Product(Base):
    price = Column(Float, default =0.0)
    image = Column(String(300), default="https://res.cloudinary.com/dy1unykph/image/upload/v1740037805/apple-iphone-16-pro-natural-titanium_lcnlu2.webp")
    cate_id = Column(Integer,ForeignKey(Category.id) , nullable =True)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        c1 = Category(name = "Laptop")
        c2 = Category(name="Điện thoại")
        c3 = Category(name="Linh kiện")
        c4 = Category(name="Máy tính bản ")

        db.session.add_all([c1,c2,c3,c4])

        with open("data/product.json", encoding="utf8") as f:
            products = json.load(f)

            for p in products:
                prod = Product(**p)
                db.session.add(prod)
        db.session.commit()