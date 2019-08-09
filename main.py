from sys  import exit

def lighthouse():
    print("Entry restricted!")
    exit(0)
<<<<<<< HEAD

def west():
=======
def north():
    while True:
        print("Where do you want to move from here?")
        move = input(""Enter 'up' or 'down': "")
        if "up" in move:
            boom()
        else:
            groom()
def south():
    while True:
        print("Where do you want to move from here?")
        move = input(""Enter 'up' or 'down': "")
        if "up" in move:
            boom()
        else:
            groom()

def east():
>>>>>>> 7013ffb2665af68c5ad1d7bfa794e7d6fbcd5c3d
    while True:
        print("Where do you want to move from here?")
        move = input("Enter 'up' or 'down': ")
        if "up" in move:
            boom()
        else:
            groom()
<<<<<<< HEAD
def groom():
    print("Welcome to the underground kingdom!")
def boom():
    print("Welcome to the sky, are you ready to fly?")
west()
=======
def west():
    while True:
        print("Where do you want to move from here?")
        move = input(""Enter 'up' or 'down': "")
        if "up" in move:
            boom()
        else:
            groom()

            
>>>>>>> 7013ffb2665af68c5ad1d7bfa794e7d6fbcd5c3d
