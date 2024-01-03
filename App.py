from Models import *

print("Apps.py works")


if __name__ == '__main__':
    with Session(engine) as session:
        first_selection = input('''
What would you like to do?
1) See all post
2) Find a post
3) add Post
''')  