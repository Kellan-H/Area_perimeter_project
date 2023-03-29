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
        shape = "Parallelogram"
        print("You have chosen " + shape)
        return True
    elif value == "5":
        shape = "Triangle"
        print("You have chosen " + shape)
        return True
    else:
        print("Whoops, please select a number 1-5")
        return False

def perimeter_area(value_2):
    if value_2 == "1":
        tool = "Perimeter"
        print("You have decided to use the tool " + tool)
        return True
    elif value_2 == "2":
        tool = "Area"
        print("You have decided to use the tool " + tool)
        return True
    else:
        print("Whoops, please select either number 1 or 2")
        return False

#Main Program
valid_shape = False
while valid_shape == False:
    value = input("What is your shape? Press:\n1. For Circle\n2. For Square\n3. For Rectangle\n4. For Parallelogram\n5. For Triangle\n")
    if is_valid(value):
        valid_shape = True



valid_tool = False
while valid_tool == False:
    value_2 = input("\nWhat would you like to calculate, Press:\n1. For perimeter\n2. For area\n")
    if perimeter_area(value_2):
        valid_tool = True