from flask import Flask
from nagiosapi.blueprints import api

app = Flask(__name__)
app.register_blueprint(api)
