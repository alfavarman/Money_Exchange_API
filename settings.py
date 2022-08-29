from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost/rates"
db = SQLAlchemy(app)


CONSTANT1 = "http://api.nbp.pl/api/exchangerates/rates/a/"
