#!/usr/bin/python2.7
# Clay Haberly 4/24/2018

import os
import sys
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
        __tablename__ = 'user'

        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        email = Column(String(250), nullable=False)
        picture = Column(String(250))

        @property
        def serialize(self):
                """Return object data in easily serializeable format"""
                return {
                        'id': self.id,
                        'name': self.user_name,
                        'email': self.user_email,
                        'picture': self.user_pic,
                }


class Category(Base):
        __tablename__ = 'category'

        id = Column(Integer, primary_key=True)
        category_name = Column(String(80), nullable=False)
        image = Column(String(250))
        user_id = Column(Integer, ForeignKey('user.id'))
        user = relationship(User)

        @property
        def serialize(self):
                """Return object data in easily serializeable format"""
                return {
                        'category_name': self.category_name,
                        'id': self.id,
                        'image': self.image,
                }


class CategoryItem(Base):
        __tablename__ = 'category_item'

        id = Column(Integer, primary_key=True)
        item_name = Column(String(80), nullable=False)
        season = Column(String(250))
        description = Column(String(250))
        price = Column(String(8))
        created_date = Column(DateTime, default=datetime.datetime.utcnow)
        category_id = Column(Integer, ForeignKey('category.id'))
        category = relationship(Category)
        user_id = Column(Integer, ForeignKey('user.id'))
        user = relationship(User)

        @property
        def serialize(self):
                """Return object data in easily serializeable format"""
                return {
                        'item_name': self.item_name,
                        'description': self.description,
                        'id': self.id,
                        'price': self.price,
                        'season': self.season,
                        'created_date': self.created_date,
                        }


engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
