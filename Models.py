from sqlalchemy import Column, Integer, String, create_engine, func, Boolean
from sqlalchemy.orm import Session, declarative_base, validates

Base = declarative_base()

def dialog():
    print("dialog funcion works")
    hoist()
    




print("Your most recent bit of code didn't break the entire program")

class User(Base): 
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True )
    name = Column(String)
    logged_in = Column(Boolean)  ### Will event be a bool.  does it need to be imported
    #def __repr__(self):
    #    return f"{self.name},{self.logged_in}"
  


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
        all_users = session.query(User).all()
        #print(all_users)
    
    def hoist():
        print("function hoisted")
    
    dialog()