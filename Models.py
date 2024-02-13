from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, validates
from sqlalchemy.exc import IntegrityError


Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False )
    user_name = Column(String, nullable=False )
    password  =Column(String, nullable=False )
    email = Column(String, nullable=False )
    tier = Column(Integer, nullable=False)

    ####relationships 4858
    ###validates at 5427 to 10609
    ##113 = CRUD
#class Meals(Base):
 #   pass

#class Foods(Base):
    
    def __repr__(self):
        return f"{self.name}: user_name {self.user_name}"

if __name__ == "__main__":

    
    engine = create_engine('sqlite:///planner.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("\n") 
    print("Welcome to Meal Planner")

    def user_list(id_of_logged_in_user, tier_of_logged_in_user):
        print("userlist")
        users = session.query(User).all()
        for user in users:
            print(f"ID:{user.id}, Name: {user.name}, Email:{user.email}")
        if tier_of_logged_in_user == 2:
            halt = input("Hit Enter to Continue")
        elif tier_of_logged_in_user == 3:
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
        print(tier_of_logged_in_user)

        logged_in = True
        while logged_in == True:
            print(id_of_logged_in_user)
            print(tier_of_logged_in_user)
            print("Please make your selection: ")
            print("   Enter 1 to create a meal: ")
            print("   Enter 2 to update your information: ")
            print("   Enter 3 to log out: ")
            if tier_of_logged_in_user != 1:
                print("    Enter 4 to see list of users: ")

            user_input = input(":")
            if int(user_input) == 3:
                print("Come back soon!")
                #main()
                logged_in = False
            elif user_input == '2':
                update_info(id_of_logged_in_user, tier_of_logged_in_user)
            elif user_input == '1':
                create_meal()
            elif user_input == '4' and tier_of_logged_in_user>1:
                user_list(id_of_logged_in_user, tier_of_logged_in_user)
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
            password = input("Please enter your password")

      

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
   
