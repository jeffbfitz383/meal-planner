import datetime
from sqlalchemy import Column, Integer, String, Date, Time, Float, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

meal_food_association = Table(
    "meal_food_association",
    Base.metadata,
    Column("meal_id", Integer, ForeignKey("meals.id")),
    Column("food_id", Integer, ForeignKey("foods.id"))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_name = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)
    tier = Column(String)
    meals = relationship("Meal", back_populates="user")

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Integer)
    time = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="meals")

    foods = relationship("Food", secondary=meal_food_association, back_populates="meals")

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    daily_percent = Column(Float)
    meals = relationship("Meal", secondary=meal_food_association, back_populates="foods")
    
    def __repr__(self):
        return f"{self.name}: user_name {self.user_name}"

if __name__ == "__main__":

    
    engine = create_engine('sqlite:///planner.db')

    Base.metadata.create_all(engine)
    #User.__table__.drop(engine)
    #Meal.__table__.drop(engine)
    #Food.__table__.drop(engine)


    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("\n") 
    print("Welcome to Meal Planner")

    def create_food(id_of_logged_in_user, tier_of_logged_in_user):
        name = input("Please enter the name of the food you would like to add: ")

        new_food = Food(name=name, daily_percent = 5)
        session.add(new_food)
        session.commit()






    def update_food(id_of_logged_in_user, tier_of_logged_in_user):
        print("Please make a selection")
        print("Enter 1 to create a food:")
        print("\n")
        selection = input(":")

        if selection == '1':
            create_food(id_of_logged_in_user, tier_of_logged_in_user)


    def create_meal(id_of_logged_in_user):
        in_create_meal = True
        while in_create_meal:
            name = input("What would you like to name this meal?: ")
            year = input("Please enter the year this meal will be eaten: ")
            month = input("Please enter the month of the meal in a number format: ")
            day = input("Please enter the day of the month: ")
            hour = input("Input the hour of day in military time ie. 23 = 11 pm: ")
            minute = input("Please enter the number of minutes past the hour ie. 45 for 8:45: ")
            
            int_year = int(year)
            int_month =int(month)
            int_day = int(day)
            int_hour = int(hour)
            int_minute = int(minute)



            date = (datetime.datetime(int_year, int_month, int_day) - datetime.datetime(2024,1,1)).days + 1
            time = ((int_hour * 60)+ int_minute)

            print("Please include the number of the food for the first food in your meal. :")
            query = session.query(Food).all()
            for record in query:
                print(f"{record.id}: Name: {record.name}, daily percent: {record.daily_percent}")
            #food_input = input(": ")
            food_input = '2'
            print(food_input)
            #next_food = Food
              
            #

            


            new_meal = Meal(name=name, date=date, time=time, user_id = 5 )
            new_meal.foods.append(food_input)
            print(new_meal)
            session.add(new_meal)
            session.commit()



            
            print("Would you like to make another meal?: ")
            user_input = input("Enter Y for yes or N for no: ")
            if user_input == 'N':
                in_create_meal = False

    def user_list(id_of_logged_in_user, tier_of_logged_in_user):
        print("userlist")
        users = session.query(User).all()
        for user in users:
            print(f"ID:{user.id}, Name: {user.name}, Email:{user.email}")
        if tier_of_logged_in_user == '2':
            halt = input("Hit Enter to Continue")
        elif tier_of_logged_in_user == '3':
            in_mod = True
            while in_mod == True:
                print("Would you like to update a user?:")
                mod = input("Type Y for yes or N for no.: ")
                if mod == 'N':
                    in_mod = False
                elif mod =="Y":
                    choice = input("Please enter the ID# of the user you would like to change:")
                    int_choice = int(choice)
                    print("Make a selection:")
                    print("Select 1 to delete a user or 2 to update the user's tier:\n")
                    selection = input(": ")
                    
                    for user in session.query(User):
                        if user.id == int_choice:
                            if selection == '1':
                                session.delete(user)
                            elif selection == '2':
                                new_tier = input("To what tier would you like to update the member?: ")
                                user.tier = int(new_tier)
                    session.commit()
                    


    def update_info(id_of_logged_in_user, tier_of_logged_in_user):
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

            if user_input == '5':
                in_update = False
            elif user_input =='1':
                new_name = input("Enter your new name: ")
                for user in session.query(User):
                    if user.id == id_of_logged_in_user:
                        user.name = new_name
                session.commit()
            elif user_input == "2":
                new_user_name = input("Enter your new user name:")
                for user in session.query(User):
                    if user.id == id_of_logged_in_user:
                        user.user_name = new_user_name
                session.commit()
            elif user_input == "3":
                new_password = input("Enter your new password:")
                for user in session.query(User):
                    if user.id == id_of_logged_in_user:
                        user.password = new_password
                session.commit()
            elif user_input == "4":
                new_email = input("Enter your new email:")
                for user in session.query(User):
                    if user.id == id_of_logged_in_user:
                        user.email = new_email
                session.commit()
            elif user_input == "6":
                cancel = input("Type Yes to confirm you really want to cancel:")
                if cancel == 'Yes':
                    for user in session.query(User):
                        if user.id == id_of_logged_in_user:
                            session.delete(user)
                    session.commit()



    def logged_in(id_of_logged_in_user, tier_of_logged_in_user):

        logged_in = True
        while logged_in == True:
            print("Please make your selection: ")
            print("   Enter 1 to create a meal: ")
            print("   Enter 2 to update your information: ")
            print("   Enter 3 to log out: ")
            if int(tier_of_logged_in_user) > 1:
                print("   Enter 4 to see a list of users: ")
            if int(tier_of_logged_in_user) > 2:
                print( "   Enter 5 to modify a food: ")

            user_input = input(":")
            if int(user_input) == 3:
                print("Come back soon!")
                #main()
                logged_in = False
            elif user_input == '2':
                update_info(id_of_logged_in_user, tier_of_logged_in_user)
            elif user_input == '1':
                create_meal(id_of_logged_in_user)
            elif int(user_input == '4' and tier_of_logged_in_user)>1:
                user_list(id_of_logged_in_user, tier_of_logged_in_user)
            elif int(user_input == '5' and tier_of_logged_in_user)>2:
                update_food(id_of_logged_in_user, tier_of_logged_in_user)
            else:
                print("please enter a valid input of either 1, 2, or 3.")

    
    def registration():
        print("\n")
        name = input("Please enter your name:")
        email = input("Please enter your email: ")
        user_name =input("Please create a username: ")
        password = input("Please make up a password:")

        new_user = User(name=name, user_name=user_name, password=password, email=email, tier=1 )
        session.add(new_user)
        session.commit()

        print(f"Congratulations {name} on becoming a part of the Meal Planner Family!\n")
        


    def loggin():
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


        
    
    in_app = True
    while in_app == True:

            #print(f"Congratulations {name} on becoming a part of the Meal Planner Family!")
    
            
        print("\n") 
        print("Enter:")
        print("\n")
        print("   1 to create and account: ")
        print("   2 to log in: ")
        print("   3 to exit: ")
        print("\n")
        
        user_input = input("Enter the number of your selection: ")

        if user_input == '3':
            print('\n')
            print('Thank you for visiting Meal Planner')
            print("See you next time!")
            print("\n")
            
            in_app = False
        elif user_input == '1':
            registration()
        elif user_input== '2':
            loggin()

        else:
            print("\n")
            print("Please enter a valid selection of either 1, 2, or 3")
   
