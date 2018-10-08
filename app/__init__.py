from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
#workaround for circular import, so it is declared after initializing app variable
from app import routes

