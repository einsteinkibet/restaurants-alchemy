from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Create a database connection
engine = create_engine('mysql+mysqlconnector://root:qwerty123@localhost/restaurants')

Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create sample instances
restaurant1 = Restaurant(name="einstein", price=3)
restaurant2 = Restaurant(name="Enashipai", price=2)
customer1 = Customer(first_name="Daniel", last_name="Mwangi")
customer2 = Customer(first_name="Harun", last_name="Kimani")

# Add instances to the session
session.add_all([restaurant1, restaurant2, customer1, customer2])
session.commit()

# Create sample reviews
review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer1)
review3 = Review(star_rating=3, restaurant=restaurant1, customer=customer2)
review4 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)

# Add reviews to the session
session.add_all([review1, review2, review3, review4])
session.commit()

# Close the session
session.close()
