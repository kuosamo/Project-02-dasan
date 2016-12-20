# -*- coding: utf-8 -*-

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, CHAR, Date, String, Time, Index, DateTime, TIMESTAMP, func
from sqlalchemy.dialects.mysql import INTEGER, BIT, TINYINT, TIME, DOUBLE, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Mysql DB modeling
class Dasan(Base):
    __tablename__ = 'DB'
    ID                  = Column(Integer, primary_key = True, nullable = False,
                                                            autoincrement = True)
    question            = Column(TEXT, nullable = False)
    directory           = Column(String(100), nullable = False)
    crawl_time          = Column(DateTime, nullable = False)
