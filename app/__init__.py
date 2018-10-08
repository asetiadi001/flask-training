from flask import Flask

app = Flask(__name__)

#workaround for circular import, so it is declared after initializing app variable
from app import routes

