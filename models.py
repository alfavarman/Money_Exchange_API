from sqlalchemy import Column, Float, String, Date
from settings import db


class CurrateA(db.Model):
    __tablename__ = 'currate'
    code = Column(String, primary_key=True)
    rate = Column(Float)
    date = Column(Date, primary_key=True)

