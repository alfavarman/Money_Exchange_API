from settings import db
from sqlalchemy import Column, Date, Float, String


class Currate(db.Model):
    __tablename__ = "currate"
    code = Column(String, primary_key=True)
    rate = Column(Float)
    date = Column(Date, primary_key=True)
