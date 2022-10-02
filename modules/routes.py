from flask import render_template, request

from app import app
from mocks import *
import find

server_host = ""
dev_host = "127.0.0.1:5000"

@app.route("/")
@app.route("/<name>")
def index(name='Anonymous'):
    return f"Hello {name}!!"


@app.route("/search/", methods=('GET', 'POST'))
def search():
    characteristics = []
    # print(product_list)
    if(request.method == 'POST'):
        query = request.form["query"]
        print(query)
        # country_name = request.form["country"]
        # category = request.form["category"]
        # characteristics = list(
        #     map(lambda x: x.split("="),
        #         request.form["characteristics"].split(",")))
        
        # search projects
        result = find.search(query, country_name = "", category = "", params = [])
        print(result)

        # return f"query = {query}<br>params = {params}"
        return render_template('search.html', product_list=product_list, characteristics=characteristics)
    # elif(request.method == "GET"):
    #     # characteristics = None
    return render_template('search.html', product_list=product_list, characteristics=characteristics)


@app.route("/product/<id>")
def product_page(id):

    # find project by id

    return render_template('product.html', product=product_a)


@app.route("/saler/<inn>")
def saler(inn):

    # find saler

    return f"saler with inn:{inn}"
