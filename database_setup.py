import sys 
import os 
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine 
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import relationship 

# Gets base class 
Base = declarative_base() 

# Define restaurant class 
class Restaurant(Base):   

    __tablename__ = 'restaurant' 

    # Restaurant table attributes 
    id = Column(Integer, primary_key=True) 
    name = Column(String(80), nullable=False) 


# Define menu item class 
class MenuItem(Base): 
    __tablename__ = 'menu_item' 

    # MenuItem table attributes
    id = Column(Integer, primary_key=True) 
    name = Column(String(80), nullable=False) 
    price = Column(String(80), nullable=False) 
    description = Column(String(250), nullable=False) 

    # Foreign key 
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

    # Define relationship between MenuItem and Restaurant 
    restaurant = relationship(Restaurant) 

# Create SQLite database 
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)