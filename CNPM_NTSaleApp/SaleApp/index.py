from flask import  Flask, render_template, request
import dao

from SaleApp import app


@app.route("/")
def index():
    q = request.args.get('q')
    cate_id = request.args.get('cate_id')
    cates = dao.load_category()
    prods = dao.load_product(q,cate_id)
    return render_template('index.html', cates= cates, prods = prods)

@app.route("/products/<int:id>")
def detail(id):
    return render_template('product-detail.html', prods = dao.get_Product_By_Id(id))

@app.route("/login")
def login_my_user():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)