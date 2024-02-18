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

    ##TODO validations

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)
    foods = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="meals")

    #TODO validations
    
    

class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    precent_protein = Column(Integer, nullable=False)
    percent_calcium =Column(Integer, nullable=False)

    #TODO validations

if __name__ == "__main__":
    engine = create_engine('sqlite:///planner.db')
    Base.metadata.create_all(engine)
    # User.__table__.drop(engine)
    # Meal.__table__.drop(engine)
    # Food.__table__.drop(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    #Owen =User(name = "Owen", email = "Owen@Minecraft.com", user_name = "1", password = "1", tier = 3)
    
   # Riley =User(name = "Riley", email = "Riley@bb.com", user_name = "1", password = "1", tier = 3)
    #session.add(Owen)
   # session.commit()

   

#to do create a 

#####end to create meal ################

    #brunch = Meal(name= "Brunch", date =50, time =50, foods = "bread", user_id = 2 )
    #breakfast = Meal(name= "Breakfast", date =50, time =50, foods = "eggs", user_id = 1 )
    #lunch = Meal(name= "Lunch", date =50, time =50, foods = "cheese", user_id = 1 )
    #dinner = Meal(name= "Dinner", date =50, time =50, foods = "meat", user_id = 1 )
    #session.add_all([breakfast, lunch, dinner])
    #session.commit()
#to do print
   # meals = session.query(Meal).all()
   # for meal in meals:
   #     print(f"{meal.name} - User: {meal.user.name}")




#TODO Meal table CRUD functions
#TODO Food table CRUD functions


##############Beginning of User Table CRUD functions##################
#TODO logged in screen

#TODO log in screen start
    def log_in():
        pass
        #TODO add functinality
#TODO log in screen end



    def new_user():
        pass
        #TODO add functionality




##############End of User Table CRUD funcions#########################



#############beginning of main menu fuctions#############

    def print_main():
        
        print("Press 1 to create and account.")
        print("press 2 to log in.")
        print("press 3 to exit\n")

    def goodbye_main():
        print("Thank you for visiting Meal Planner!")
        print("See you next time! :) \n")


    def main():
        print("Welcome to Meal Planner.\n")
        in_main = True
        while in_main == True:
            print_main()
            user_input = input(":")
            if user_input == "3":
                in_main = False
                goodbye_main()
            elif user_input == "2":
                log_in()
            elif user_input == "1":
                new_user()
            else:
                print("invalid input. Please select an input from the menu.\n")
                print("Main Menu\n")
############### end main menu functions  #################

    main()

