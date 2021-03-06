#######################################################
# 
# User.py
# Python implementation of the Class User
# Generated by Enterprise Architect
# Created on:      21-Sep-2020 10:28:08 PM
# Original author: natha
# 
#######################################################
from sqlalchemy import Column
from FreeTAKServer.model.SQLAlchemy.Root import Base
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from FreeTAKServer.model.SQLAlchemy.Event import Event
from FreeTAKServer.model.SQLAlchemy.system_user import SystemUser

class User(Base):
# default constructor  def __init__(self):  

    """sqlalchemy object of table of connected users and their information
    """
    __tablename__ = "User"
    uid = Column(String(25), primary_key = True)
    callsign = Column(String)
    CN = Column(String, nullable=True)
    IP = Column(String)
    CoT_id = Column(String, ForeignKey("Event.uid"))
    CoT = relationship(Event, uselist=False, cascade="all, delete", backref="User")