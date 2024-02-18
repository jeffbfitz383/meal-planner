from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, sessionmaker, validates

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    tier = Column(Integer, nullable=False)
    meals = relationship("Meal", back_populates="user")

    ##todo validations

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)
    foods = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship("User", back_populates="meal")

    #todo validations
    
    

class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    precent_protein = Column(Integer, nullable=False)
    percent_calcium =Column(Integer, nullable=False)

    #todo validations

if __name__ == "__main__":
    engine = create_engine('sqlite:///planner.db')
    Base.metadata.create_all(engine)
    # User.__table__.drop(engine)
    # Meal.__table__.drop(engine)
    # Food.__table__.drop(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


#create a user
#create a meal
#print

##Todo test relationships
##Todo main Cli