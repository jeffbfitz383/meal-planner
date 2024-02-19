Title- Meal Planners

Purpose- Meal allows the user to maintain a personal meal calendar were meals can be create from a list of available foods.  The meals can be edited, deleted, referenced by the user at a later time.  The meals the user creates are used by meal planner to provide nutritional feed back that is useful in creating future meals.

Getting started
    -from CLI terminal cd into meal-planner
    -cd into lib
    -run python3 main.py

Navigation - Navigation is easy.  Each screen is a list of numerated choices. At any screen enter the number of your select and hit enter.  Each screen will provide several choices to move to a new screen and one choice to navigate back to the previous screen.  Below is a map of all the screens.  Children screens are indented immediatly under it parent screen

-create account (Must be done the first time you visit meal planner)
-log in
    -log out(logs the user out of their profile)
    -update info(allows users update any info entered during the registration process)
    -see meals (allows the user to see the meals they have alreay created)
    -create meal (allows the user to create a new meal through a series of prompts and a food list )
    -update foods(allows to user to make any updates to the list of available foods.  Only users with tier 3(administrative rights) can access update foods)
    -delete meal(allows the user to delete any meals they have created through a series of prompts)
    -update meal(allows the user to selectively update any piece of information on a meal they alredy created)
    -view users(allows the user to view the info of other active members(only available to tier 3 admnistrators))
-exit (To leave meal-planner)




Some prompts may have specific requirements.
    during registration
        name- must be text greater than one charater
        email- must be text and a valid email address
        username - must be greater than or equal to 4 characters
        password - msut be greater than or equal to 8 character

    during log in
        you will be prompted for the username and the password you created.

    when create a meal
        name - must be text of 1 to 29 characters inclusive
        date = must be a number
        time = must be a number from 0 to 1440 inclusive

    when an admin updates foods
        name - must be between 1 and 30 charters
        percent protein - must be an integer from 0 to 100
        percent calcium - must be an integer from 0 to 100




    When the meal creation proess between each prompt meal-planner will regenerate the table of available foods sort according to the user's greatest nutricional gaps.
    
    The Code-

    The code only uses one file named main.py
    It is recommended that when viewing coding you only leave one funcion open at a time with the arrow tabs.

list of function in order of appearance in the code




class User(Base):  ## Defines the User table
    User validations

meal_food_table   ## acts as a join table between the meal and food table

class Meal(Base): ## Defines Meal table
    Meal validations

class Food(Base)
    Food validations

see_foods()  ## Prints a table of the available foods
sort_foods() ## Sorts all foods in the ascending order of the users most deficient nutrient
week_sort()  ## Sorts foods by greatest deficiency base of meal data for the past week
unpack_meals()  ## accepts a meal id and converts the appended foods into a string
unpack_date()  dates are stored as a single integer consistent the number of days since jan 1 of 1970 that they meal is to be eaten.  This function converts
    that to a recognizable date
see_meals() shows every meal created by the logged in user
delete_meal() allows the user to delete a specific meal
update_meal() allows the user to change any component to an existing meal
create_meal() allows to user to creat a new meal
change_calcium() updates the total calcium in a pending meal every time a new food is added.
change_protein() updates the total protein in a pending meal ever time a new food is added
change_food_name() is used to update the name of a food
delete_food() is used to delete foods from the Food table
creat_new_food() is used to add a new food to the food table
update_foods() presents the user with different options for updating foods
update_user() is used to update any info on an existing user
view_user() is used to view all users in the User table
logged_in() runs the main table the user see immediatley after logging in
log_in() runs the log in process
new_user() runs the registration process
print_main() prints the options on the starting menu
goodbye__main() prints the salutation once the user opts to exit meal-planner
main() runs first set of user promps

  

        













    

    



   


        

        

        

            


        

  











       
























