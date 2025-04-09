import enum
from typing import Any
from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey, Enum as PgEnum
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared
from api import db

class Role(enum.Enum):
    admin: str = "admin"
    player: str = "player"
    owner: str = "owner"

    def as_dict(self) -> dict[str, str]:
        return {
            "role": self.name,
        }
    
class WeekType(enum.Enum):
    normal: str = "normal"
    spoiler: str = "spoiler"

    def as_dict(self) -> dict[str, str]:
        return {
            "week_type": self.name
        }
    
class User(db.Model):
    __tablename__: str = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    hashed_password = Column(String(100), nullable=False)
    role = Column(PgEnum(Role), nullable=False)

    records: _RelationshipDeclared[Any] = relationship("Record", backref="user", cascade="all, delete", passive_deletes=True)

    def as_dict(self) -> dict:
        return {
            "user_id" : self.user_id,
            "user_name" : self.user_name,
            "hashed_password" : self.hashed_password,
            "role" : self.role.name if self.role else None
        }
    
class Week(db.Model):
    __tablename__: str = 'weeks' 

    week_id = Column(Integer, primary_key=True)  
    week_number = Column(Integer, nullable=False)
    week_type = Column(PgEnum(WeekType), nullable=False)
    title = Column(String(100), nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)
    perma_link = Column(String, nullable=False)
    seed = Column(String, nullable=False)

    records: _RelationshipDeclared[Any] = relationship("Record", backref="week", cascade="all, delete")

    def as_dict(self) -> dict:
        return {
            "week_id" : self.week_id,
            "week_number" : self.week_number,
            "week_type" : self.week_type.name,    
            "title" : self.title,
            "start_date" : self.start_date,
            "end_date" : self.end_date,
            "perma_link" : self.perma_link,
            "seed" : self.seed,
        }
    
class Record(db.Model):
    __tablename__: str = 'records'  

    record_id = Column(Integer, primary_key=True) 
    points = Column(Integer, nullable=False, default=0)
    completion_time = Column(Time, nullable=False)
    vod_link = Column(String(200), nullable=True)
    comments = Column(String, nullable=True)

    week_id = Column(Integer, ForeignKey("weeks.week_id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)  

    def as_dict(self) -> dict:
        return {
            "record_id": self.record_id,
            "points": self.points,
            "completion_time": self.completion_time.strftime('%H:%M:%S.%f'),
            "vod_link": self.vod_link,
            "comments": self.comments,
            "week_id": self.week_id,
            "user_id": self.user_id
        }
