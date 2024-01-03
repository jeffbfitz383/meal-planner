from sqlalchemy import Column, Integer, String, create_engine, func, Boolean
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()



print("Your most recent bit of code didn't break the entire program")

class User(Base): 
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True )
    name = Column(String)
    logged_in = Column(Boolean)  ### Will event be a bool.  does it need to be imported

class Meals(Base):
    __tablename__="Meals"
    id = Column(Integer, primary_key = True)


if __name__ == '__main__':
    engine = create_engine('sqlite:///meal_planner.db')
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        u1 = User(
            name = "Leonardo",
            logged_in = 0
        )
        session.add(u1)
        session.commit()