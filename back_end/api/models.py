from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from api import db

class Users(db.Model):
    __tablename__: str = "users"



class Records(db.Model):
    __tablename__ : str = "records"


class Weeks(db.Model):
    __tablename__ : str = "weeks"