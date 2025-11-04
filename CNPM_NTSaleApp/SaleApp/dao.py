import json
from SaleApp.models import Category, Product
from SaleApp import app

def load_category():
    #with open("data/category.json", encoding="utf-8") as f:
    #    return json.load(f)
    return Category.query.all()
def load_product(q=None,cate_id=None, page=None):
    #with open("data/product.json", encoding="utf-8") as f:
     #   prods = json.load(f)
        query = Product.query

        if q:
            query = query.filter(Product.name.contains(q))

        if cate_id:
            query = query.filter(Product.cate_id.__eq__(int(cate_id)))

        if page:
            size = app.config["PAGE_SIZE"]
            start = (int(page) -1 ) *size
            query = query.slice(start, (start+size))

        return query.all()

def get_Product_By_Id(id):
    return Product.query.get(id)


