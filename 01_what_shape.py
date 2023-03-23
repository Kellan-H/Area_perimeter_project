#Funtctions
def is_valid(value):
    if value == "1":
        shape = "Circle"
        print("You have chosen " + shape)
        return True
    elif value == "2":
        shape = "Square"
        print("You have chosen " + shape)
        return True
    elif value == "3":
        shape = "Rectangle"
        print("You have chosen " + shape)
        return True
    elif value == "4":
        shape = "Paralellogram"
        print("You have chosen " + shape)
        return True
    elif value == "5":
        shape = "Triangle"
        print("You have chosen " + shape)
        return True
    else:
        print("Whoops, please select a number 1-5")
        return False

#Main Program
valid_shape = False
while valid_shape == False:
    value = (input("What is your shape? Press:\n1. For Circle\n2. For Square\n3. For Rectangle\n4. For Paralellogram\n5. For Triangle\n"))
    if is_valid(value):
        valid_shape = True



