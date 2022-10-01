from flask import render_template, request

from app import app
from mocks import *

server_host = ""
dev_host = "127.0.0.1:5000"

@app.route("/")
@app.route("/<name>")
def index(name='Anonymous'):
    return f"Hello {name}!!"


@app.route("/search")
def search():
    # print(product_list)
    query = request.args.get('query', default="", type=str)
    country_name = request.args.get('country', default="", type=str)
    category = request.args.get('category', default="", type=str)
    params = list(
        map(lambda x: x.split("="),
            request.args.get('params', default="", type=str).split(",")))

    # search projects

    # return f"query = {query}<br>params = {params}"
    return render_template('search.html', product_list=product_list)


@app.route("/product/<id>")
def product_page(id):

    # find project by id

    return render_template('product.html', product=product_a)


@app.route("/saler/<inn>")
def saler(inn):

    # find saler

    return f"saler with inn:{inn}"
