from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

engine = create_engine('mysql+mysqlconnector://root:qwerty123@localhost/restaurants')

Base.metadata.create_all(engine)

def add_customer(first_name, last_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    customer = Customer(first_name=first_name, last_name=last_name)
    session.add(customer)
    session.commit()
    session.close()

def add_restaurant(name, price):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    restaurant = Restaurant(name=name, price=price)
    session.add(restaurant)
    session.commit()
    session.close()

def add_review(star_rating, restaurant_id, customer_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    customer = session.query(Customer).filter_by(id=customer_id).first()
    
    if restaurant and customer:
        review = Review(star_rating=star_rating, restaurant=restaurant, customer=customer)
        session.add(review)
        session.commit()
    else:
        print("Restaurant or Customer does not exist.")
    
    session.close()