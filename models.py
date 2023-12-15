from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    reviews = relationship('Review', back_populates='customer')
    
class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    
    customers = relationship('Customer', secondary='reviews')
    reviews = relationship('Review', back_populates='restaurant')
    
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

    def __init__(self, star_rating, restaurant, customer):
        self.star_rating = star_rating
        self.restaurant = restaurant
        self.customer = customer
