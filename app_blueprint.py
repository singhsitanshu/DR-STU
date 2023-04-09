from flask import Blueprint

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/')
def index():
    return home

@app_blueprint.route('/apparel')
def apparel():
    return apparel

@app_blueprint.route('/dunks')
def dunks():
    return dunks

@app_blueprint.route('/jordans')
def jordans():
    return jordans