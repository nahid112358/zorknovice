from sys  import exit

def lighthouse():
    print("Entry restricted!")
    exit(0)
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
    while True:
        print("Where do you want to move from here?")
        move = input("Enter 'up' or 'down': ")
        if "up" in move:
            boom()
        else:
            groom()
def west():
    while True:
        print("Where do you want to move from here?")
        move = input(""Enter 'up' or 'down': "")
        if "up" in move:
            boom()
        else:
            groom()

            
