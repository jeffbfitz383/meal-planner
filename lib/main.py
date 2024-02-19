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

    @validates('name')
    def validate_name(self, key, value):
        if type(value) is str and 2<= len(value):
            return value
        else: ValueError("Names must be in a text format and contain atleast 2 characters.")

    @validates('email')
    def validate_email(self, key, value):
        if type(value) is str and "@" in value and 6<= len(value):
            return value
        else: ValueError("emails must be at least 6 caracters and include a '@'. ")

    @validates('user_name')
    def validate_user_name(self, key, value):
        if type(value) is str and 4<= len(value):
            return value
        else: ValueError("a username must be of type text and contain at least 4 characters")

    @validates('password')
    def validate_password(self, key, value):
        if type(value) is str and 8<= len(value):
            return value
        else: ValueError("passwords must be at least 8 characters in length")

    @validates('tier')
    def validate_tier(self, key, value):
        if type(value) is int and 1<= value <=3:
            return value
        else: ValueError("A tier must either be 1, 2, or 3")
            

    


    ##TODO complete validations

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
    
    def see_meals(id_of_logged_in_user, tier_of_logged_in_user):
        meals = session.query(Meal).all()
        for meal in meals:
            if meal.user.id == id_of_logged_in_user:
             print(f"{meal.user.name}, {meal.name}")
            #TODO complete
    

    
    def update_user(id_of_logged_in_user, tier_of_logged_in_user):
          
        in_update = True
        while in_update == True:
            print("Make a selection:")
            print("   Enter 1 to update name: ")
            print("   Enter 2 to update your user_name: ")
            print("   Enter 3 to update your password: ")
            print("   Enter 4 to update your email: ")
            print("   Enter 5 to exit ")
            print("   Enter 6 to cancel account: ")

            user_input = input(":")
            for user in session.query(User):
                if user.id == id_of_logged_in_user:
                    if user_input == '5':
                        in_update = False
                    elif user_input == '1':
                        in_loop = True
                        while in_loop == True:

                            name_input = input("What is your new name?")
                            if type(name_input) is str and 2<= len(name_input):
                                user.name = name_input
                                in_loop = False
                            else:
                                print("Name must be text with 2 or more characters")

                    elif user_input == '2':
                        
                        in_loop = True
                        while in_loop == True:

                            user_name_input = input("What is your new  user name?")
                            if type(user_name_input) is str and 4<= len(user_name_input):
                                user.user_name = user_name_input
                                in_loop = False
                            else:
                                print("User name must be text with 4 or more characters")

                    
                    elif user_input == '3':
                       
                        in_loop = True
                        while in_loop == True:

                            password_input = input("What is your new password")
                            if type(password_input) is str and 8<= len(password_input):
                                user.password = password_input
                                in_loop = False
                            else:
                                print("password must be text with 8 or more characters")

                    elif user_input == '4':
                    
                        in_loop = True
                        while in_loop == True:

                            email_input = input("What is your new email: ")
                            if type(email_input) is str and 6<= len(email_input) and '@' in email_input:
                                user.email = email_input
                                in_loop = False
                            else:
                                print("Email must be text with 6 or more characters and include and @ symbol")

                    elif user_input == '6':
                        in_update = False
                        session.delete(user)

            session.commit()



        

        

        if user_input == '3':
            update_user_name(id_of_logged_in_user, tier_of_logged_in_user)

    def logged_in(id_of_logged_in_user, tier_of_logged_in_user):
        
        logged_in_status = True
        while logged_in_status == True:
            print("  Enter 1 to log out: ")
            print("  Enteer 2 to update info")
            print("  Enter 3 to see your meals")
            user_input = input(": ")
            if user_input == "1":
                print("come back and see us soon!")
                logged_in_status = False
            elif user_input == "2":
                update_user(id_of_logged_in_user, tier_of_logged_in_user)
            elif user_input == "3":
                see_meals(id_of_logged_in_user, tier_of_logged_in_user)


        
        #TODO update personal info
        #TODO see meals
        #TODO create meals

        #TODO update food for admin
        #TODO update users for owner


    def log_in():
        at_loggin = True
        id_of_logged_in_user = 0
        tier_of_logged_in_user = 0
        while at_loggin == True:
            print("\n")
            user_name = input("please enter your user name to login:")
            password = input("Please enter your password: ")

      

            query = session.query(User).filter(User.user_name == user_name, password == password).all()
            if query:
                for record in query:
                    id_of_logged_in_user = record.id
                    tier_of_logged_in_user = record.tier
                    at_loggin = False
                    logged_in(id_of_logged_in_user, tier_of_logged_in_user)
                
                
      
            else:
                print("password and username missmatch")




    def new_user():
        name_loop =True
        while name_loop == True:
            name = input("Please enter your name: ")
            if type(name) is str and 2<= len(name):        #class method validation is also present but I could figure out a way to maintain the loop.
                name_loop = False
            else:
                 print("A name must be a least 2 characters and in text form ")
        
        email_loop=True
        while email_loop == True:
            email = input("Please enter your email address: ")
            if type(email) is str and "@" in email and 6<= len(email):
                email_loop = False
            else:
                print("please enter a valid email address")

        user_name_loop=True
        while user_name_loop == True:
            user_name = input("Please enter your username: ")
            if type(user_name) is str and 4<= len(user_name):
                user_name_loop = False
            else:
                print("a user name must be atleast 4 characters.")

        password_loop = True
        while password_loop == True:
            password = input("Please enter your password: ")
            if type(password) is str and 8<= len(password):
                password_loop = False
            else:
                print("passwords must be atleast 8 characters")

        new_user = User(name=name, user_name=user_name, password=password, email=email, tier=1 )
        session.add(new_user)
        session.commit()

        print(f"Congratulations {name} on becoming a part of the Meal Planner Family!\n")


       




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

