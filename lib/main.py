import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table, Date, Time
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
            

    





meal_food_table = Table('meal_food', Base.metadata,
    Column('meal_id', Integer, ForeignKey('meals.id'), primary_key=True),
    Column('food_id', Integer, ForeignKey('foods.id'), primary_key=True)
)

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)
    foods = relationship("Food", secondary=meal_food_table, back_populates="meals")
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="meals")

    @validates('name')
    def validate_name(self, key, value):
        if type(value) is str and 1<= len(value) <30:
            return value
        else: ValueError("meal name must be in text for between 1 and 29 characters")

    @validates('date')
    def validate_date(self, key, value):
        if type(value) is int:
            return value
        else: ValueError("date type must be and integer")

    @validates('time')
    def validate_date(self, key, value):
        if type(value) is int and 0 <= value <= 1440:
            return value
        else: ValueError("date type must be an integer between 0 and 1440")








    
    

class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    percent_protein = Column(Integer, nullable=False)
    percent_calcium =Column(Integer, nullable=False)
    meals = relationship("Meal", secondary=meal_food_table, back_populates="foods")
    meal_id = Column(Integer, ForeignKey('meals.id'))

    @validates('name')
    def validate_name(self, key, value):
        if type(value) is str and 1<= len(value) <= 30:
            return value
        else: ValueError("name must be of type test between 1 and 30 character inclusive")

    @validates('percent_protein')
    def validate_percent_protein(self, key, value):
        if type(value) is int and 0<= value <= 100:
            return value
        else: ValueError("percent_protein must int ranging from 0 to 100")

    @validates('percent_calcium')
    def validate_percent_calcium(self, key, value):
        if type(value) is int and 0<= value <= 100:
            return value
        else: ValueError("percent_calcium must be must be int from 0 to 100")

    


    

if __name__ == "__main__":
    engine = create_engine('sqlite:///planner.db')
    Base.metadata.create_all(engine)
    # User.__table__.drop(engine)
    # Meal.__table__.drop(engine)
    # Food.__table__.drop(engine)
    Session = sessionmaker(bind=engine)
    session = Session()



   

##############start of create meals CRUD functions#############
    

    def see_foods():
        foods = session.query(Food).all()
        for food in foods:
            print(f"ID: {food.id}, Name: {food.name}, % daily protein: {food.percent_protein}% daily Calcium: {food.percent_calcium}")  #prints all foods

    def sort_foods(greatest_deficiency, id_of_logged_in_user):             ## sorts in descending by calium and protein
        print("\n")
        foods = session.query(Food).all()
        if greatest_deficiency == 1:
            sorted_foods_descending = sorted(foods, key=lambda x: x.percent_calcium, reverse=True)
            for food in sorted_foods_descending:
                print(f"ID: {food.id}, Name: {food.name}, % daily protein: {food.percent_protein}% daily Calcium: {food.percent_calcium}")
        elif greatest_deficiency == 2:
            sorted_foods_descending = sorted(foods, key=lambda x: x.percent_protein, reverse=True)
            for food in sorted_foods_descending:
                print(f"ID: {food.id}, Name: {food.name}, % daily protein: {food.percent_protein}% daily Calcium: {food.percent_calcium}")
                print("\n")

    def week_sort(id_of_logged_in_user, date):      #start count for weekely total
        week_total_calcium = 0
        week_total_protein = 0
        greatest_deficiency_week = 0


        week_back = date -7                         # goes back a day before current day
        #print(date)
        #print(week_back)
        meals = session.query(Meal).all()
        for meal in meals:
            if week_back <= meal.date < date and meal.user_id == id_of_logged_in_user:      # gets all 7 days
                for food in meal.foods:
                    print(food.name)
                    week_total_calcium = week_total_calcium + food.percent_calcium          # adds to total
                    week_total_protein = week_total_protein + food.percent_protein
        if week_total_calcium >= week_total_protein:                                        # entire loop identifies which is greater
            greatest_deficiency_week = 2
            print("your greatest deficiency for the week is protein")
        else:
            greatest_deficiency_week = 1
            print("Your greatest deficiency for the week is calcium")
        sort_foods(greatest_deficiency_week, id_of_logged_in_user)
        print("\n")   




    def unpack_meals(meal_id):                          # converts all meals under meal id to array and then a comma sperated string
        all = []

        meals = session.query(Meal).all()
        for meal in meals:
            if meal.id == meal_id:
                for food in meal.foods:
                    all.append(food.name)
        comma_separated_string = ", ".join(all)
        return comma_separated_string

    def unpack_date(date):                                                # converts epoch date to date
        days_since_epoch = 19773
        epoch_date = datetime.datetime(1970, 1, 1)
        target_date = epoch_date + datetime.timedelta(days=days_since_epoch)
        formatted_date = target_date.strftime('%Y-%m-%d')
        return formatted_date
        

    def see_meals(id_of_logged_in_user, tier_of_logged_in_user):            # prints an table for all meals of a particular user
        users = session.query(User).all()
        for user in users:
            if user.id == id_of_logged_in_user:

                print(f"Showing meals for user {user.name}")
        meals = session.query(Meal).all()

        
        for meal in meals:
       
            if meal.user.id == id_of_logged_in_user:
                date = unpack_date(meal.date)
                hour = int(meal.time/60)
                minute =(meal.time%60)
                half_time = 'am'
                if hour >12:
                    hour = hour -12
                    half_time = 'pm'
                else:
                    hour = hour
                    half_time = 'am'
                meals_unpacked =unpack_meals(meal.id)
             
                print(f"ID: {meal.id}, Meal name: {meal.name}, Date: {date}, Time: {hour}:{minute} {half_time}, Meals: ({meals_unpacked})")
                print("\n")

    def delete_meal(id_of_logged_in_user, tier_of_logged_in_user):          # user can delete one of their meals

        print("Enter the ID# of the meal you would like to delete")
        see_meals(id_of_logged_in_user, tier_of_logged_in_user)
        print("\n")
        user_input = input(": ")
        meals = session.query(Meal).all()
        for meal in meals:
            if meal.id == int(user_input):
                session.delete(meal)
        session.commit()

    def add_protein(int_food):                                       # determines how much protein to add every time a food is added to a meal 
        foods = session.query(Food).all()
        for food in foods:
            if food.id == int_food:
                return food.percent_protein

    def add_calcium(int_food):
        foods = session.query(Food).all()                            # determines how much calcium to add
        for food in foods:
            if food.id == int_food:
                return food.percent_calcium

        
    def update_meal(id_of_logged_in_user, tier_of_logged_in_user):
        see_meals(id_of_logged_in_user, tier_of_logged_in_user)
        print("Enter the id# of the meal you want to update. ")
        user_input = input(": ")
        for meal in session.query(Meal):
            if meal.id == int(user_input):
                print("You will be prompted to update each value in the above meal")
                print("Please Enter the new value")
                print("If the value is to remane the same re-enter the original value")
                new_name = input("What is the new name of the meal: ")
                year= input("Please enter the correct year: ")
                month = input("Please enter the correct month:")
                day = input("Please enter the correct day")
                hour = input("Please enter the correct hour in military time:")
                minute = input("Please enter minutes past the hour: ") 


                int_year = int(year)
                int_month =int(month)
                int_day = int(day)
                int_hour = int(hour)
                int_minute = int(minute)
                
                date = (datetime.datetime(int_year, int_month, int_day) - datetime.datetime(1970,1,1)).days + 1
                time = ((int_hour * 60)+ int_minute)

                meal.name = new_name
                meal.date = date
                meal.time = time

                all = []                                                                   # prints all meals
                for meal in session.query(Meal):
                    if meal.id == int(user_input):
                        for food in meal.foods:
                            all.append(food.name)
                
                print(all)

                food_to_remove = input("please enter the food to remove or hit enter to skip:")  # add and delete foods to an existing meal
                meal.foods = [food for food in meal.foods if food.name != food_to_remove]
                print(meal.foods) 


                foods = session.query(Food).all()
                for food in foods:
                    print(f"ID: {food.id}, Name: {food.name}, % daily protein: {food.percent_protein}% daily Calcium: {food.percent_calcium}")

                add_choice =input("would you like to add any of these foods? Hit Y for yes on any other key for no: ")
                if add_choice == 'Y':

                    food_to_add = int(input("please enter the id of the food you would like to add or hit enter to skip: "))
                    food = session.query(Food).filter_by(id=food_to_add).first()
                    print(food)
                    print(meal.id)

                    if food not in meal.foods:
                        meal.foods.append(food)
                        session.commit()
                    else:
                        print("food already in list")

        session.commit()







    def create_meal(id_of_logged_in_user, tier_of_logged_in_user):
        print("you are creating a meal")

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

            date = (datetime.datetime(int_year, int_month, int_day) - datetime.datetime(1970,1,1)).days + 1
            time = ((int_hour * 60)+ int_minute)

            new_meal = Meal(name=name, date=date, time=time, user_id = id_of_logged_in_user)
            session.add(new_meal)
            food_loop = True
            one_pass = False
            total_protein = 0
            total_calcium = 0
            greatest_deficiency = 0
            while food_loop == True:
                
                print("press 1 to add a food to your meal")
                print("Press 2 to submit meal")
                user_input = input(": ")
                if user_input == '2':                                     # determines whethor the first meal has been added
                    food_loop = False
                else:
                    if one_pass == False:
                        #see_foods()
                        week_sort(id_of_logged_in_user, date)
                    elif one_pass == True:
                        print("not first pass")
                        sort_foods(greatest_deficiency, id_of_logged_in_user)
                    print("Please enter the item # of the food you would like to add: ")
                    food_input = input(": ")
                    int_food = int(food_input)
                    new_food = session.get(Food, int_food)
                    new_meal.foods.append(new_food)
                    session.commit()
                    added_protein = add_protein(int_food)
                    total_protein = total_protein + added_protein
                    added_calcium = add_calcium(int_food)
                    total_calcium = total_calcium + added_calcium
                    if total_protein > total_calcium:
                        greatest_deficiency = 1
                    else:
                        greatest_deficiency = 2
                    print(greatest_deficiency)
                    #add_calcium()
                one_pass = True
                print(one_pass)
                    



            


                in_create_meal = False
            

#####end to create meal ################

    #brunch = Meal(name= "Brunch", date =50, time =50, foods = "bread", user_id = 2 )
    #breakfast = Meal(name= "Breakfast", date =50, time =50, foods = "eggs", user_id = 1 )
    #lunch = Meal(name= "Lunch", date =50, time =50, foods = "cheese", user_id = 1 )
    #dinner = Meal(name= "Dinner", date =50, time =50, foods = "meat", user_id = 1 )
    #session.add_all([breakfast, lunch, dinner])
    #session.commit()





#TODO Meal table CRUD functions
###############Beginning of Food crud functions################
    def change_calcium():
        see_foods()
        print("\n")
        user_input= input("Please select the id of the food you would like to update")
        int_id = int(user_input)
        for food in session.query(Food):
            if food.id == int_id:
                new_calcium = input("What is the correct daily calcium allowance")
                food.percent_calcium = int(new_calcium)
        session.commit()


    def change_protein():
        see_foods()
        print("\n")
        user_input= input("Please select the id of the food you would like to update")
        int_id = int(user_input)
        for food in session.query(Food):
            if food.id == int_id:
                new_protein = input("What is the correct daily protein allowance")
                food.percent_protein = int(new_protein)
        session.commit()

    def change_food_name():
        see_foods()
        print("\n")
        user_input= input("Please select the id of the food you would like to rename")
        int_id = int(user_input)

        for food in session.query(Food):
            if food.id == int_id:
                new_name_input = input("What would you like the new name to be?: ")
                food.name = new_name_input
        session.commit()  



    def delete_food():
        see_foods()
        print("\n")
        user_input= input("Please select the id of the food you would like to delete")
        int_id = int(user_input)

        for food in session.query(Food):
            if food.id == int_id:
                session.delete(food)
        session.commit()
        



    def create_new_food():
        name_loop = True
        while name_loop == True:
            name = input("What is the name of the new food: ")
            if type(name) is str and 1<= len(name):
                name_loop = False
            else:
                print("food names must be in text form and be at least 1 character in length")

        protein_loop = True
        while protein_loop ==True:
            protein = int(input("Enter the percent dailey protein allowance for one serving"))
            if type(protein) is int and 0<= protein <=100:
                protein_loop = False
            else:
                print("Protein percentages must be a whole # between 0 and 100")

        ca_loop = True
        while ca_loop ==True:
            calcium = int(input("Enter the percent dailey calcium allowance for one serving"))
            if type(calcium) is int and 0<= calcium <=100:
                ca_loop = False
            else:
                print("Calcium percentages must be a whole # between 0 and 100")

        new_food = Food(name=name, percent_protein=protein, percent_calcium=calcium)
        session.add(new_food)
        session.commit()


    def update_foods(id_of_logged_in_user, tier_of_logged_in_user):

        in_update_foods = True
        while in_update_foods == True:

            print("  Enter 1 to go back to previous menu: ")
            print("  Enter 2 to create a new food: ") 
            print("  Enter 3 to update food name: ")
            print("  Enter 4 to update protein content: ")
            print("  Enter 5 to update calcium content: ")
            print("  Enter 6 to delete a food: ")


            user_input = input(": ")
            if user_input == '1':
                in_update_foods =False
            elif user_input == '2':
                create_new_food()
            elif user_input =='3':
                change_food_name()
            elif user_input =='4':
                change_protein()
            elif user_input =='5':
                change_calcium()
            elif user_input == '6':
                delete_food()
            else:
                print("enter valid input: ")






###############End of food Crud functions#############################
##############Beginning of User Table CRUD functions##################
    

    

    
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

    def view_users(id_of_logged_in_user, tier_of_logged_in_user):
        print("\n")
        
        for user in session.query(User).all():
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Tier: {user.tier}\n")


        

        

        
    def logged_in(id_of_logged_in_user, tier_of_logged_in_user):  #logged in option menu
        
        logged_in_status = True
        while logged_in_status == True:
            print("  Enter 1 to log out: ")
            print("  Enteer 2 to update info")
            print("  Enter 3 to see your meals")
            print("  Enter 4 to create a new meal")
            if tier_of_logged_in_user >1:
                print("  Enter 5 to update food: ")
            print(" Enter 6 to delete a meal: ")
            if tier_of_logged_in_user >1:
                print(" Enter 7 to view users")
            print("  Enter 8 to update meal")

            user_input = input(": ")
            print("\n")

            if user_input == "1":
                print("come back and see us soon!")
                logged_in_status = False
            elif user_input == "2":
                update_user(id_of_logged_in_user, tier_of_logged_in_user)
            elif user_input == "3":
                see_meals(id_of_logged_in_user, tier_of_logged_in_user)
            elif user_input == '4':
                create_meal(id_of_logged_in_user, tier_of_logged_in_user)
            
            elif user_input == '5' and tier_of_logged_in_user >1:
                update_foods(id_of_logged_in_user, tier_of_logged_in_user)

            elif user_input == '6':
                delete_meal(id_of_logged_in_user, tier_of_logged_in_user)
            elif user_input == '7' and tier_of_logged_in_user >1:
                view_users(id_of_logged_in_user, tier_of_logged_in_user)
            elif user_input == '8':
                update_meal(id_of_logged_in_user, tier_of_logged_in_user)
            


        

  




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

        new_user = User(name=name, user_name=user_name, password=password, email=email, tier=3 )
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

