from sqlalchemy import Column, Date, Float, String

from settings import db


class Currate(db.Model):
    __tablename__ = "currate"
    code = Column(String, primary_key=True)
    rate = Column(Float)
    date = Column(Date, primary_key=True)
