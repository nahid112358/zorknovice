from sys  import exit

def lighthouse():
    print("Entry restricted!")
    exit(0)

def west():
    while True:
        print("Where do you want to move from here?")
        move = input("Enter 'up' or 'down': ")
        if "up" in move:
            boom()
        else:
            groom()
def groom():
    print("Welcome to the underground kingdom!")
def boom():
    print("Welcome to the sky, are you ready to fly?")
west()
