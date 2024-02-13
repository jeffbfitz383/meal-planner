from Models import *

print("Apps.py works")


if __name__ == '__main__':
    with Session(engine) as session:
        main_menu = input('''
What would you like to update?
1) Users
2) meals
3) Food items
''')  