from flask import request

from app import app


@app.route("/")
@app.route("/<name>")
def index(name='Anonymous'):
    return f"Hello {name}!!"

@app.route("/search")
def search():
    query = request.args.get('query', default = "", type = str)
    country_name = request.args.get('country', default = "", type = str)
    category = request.args.get('category', default = "", type = str)
    params = list(
                map(lambda x: x.split("=") ,
                    request.args.get('params', default ="", type = str).split(",")))

    #search projects

    return f"query = {query}<br>params = {params}"

@app.route("/product/<id>")
def product_page(id):

    ### find project by id

    return f"product №{id}"

@app.route("/saler/<inn>")
def saler(inn):

    ### find saler
    
    return f"saler with inn:{inn}"