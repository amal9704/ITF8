def add(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

def calculate_triangle_area(base,height):
    return 0.5*base*height


def calculate_circle_area(radius):
    return 3.14*radius**2

def calculate_rectangle_area(lenght,width):
    return lenght*width

def main_menu():
    while True:
        selection = float(input("1. sum\n"
    "2. subtract\n"
    "3. multiply\n"
    "4. division\n"
    "5. calculate triangle area\n"
    "6. calculate circle area\n"
    "7. calculate square area\n" 
    "8. exit"))

        if selection == 1:
            num1 = float(input("enter num1:"))
            num2 = float(input("enter num2:"))
            print("result:", add(num1, num2))


        elif selection == 2:
            num1 = float(input("enter num1:"))
            num2 = float(input("enter num2:"))
            print("result:", subtraction(num1, num2))

        elif selection == 3:
            num1 = float(input("enter num1:"))
            num2 = float(input("enter num2:"))
            print("result:", multiplication(num1,num2))

        elif selection == 4:
            num1 = float(input("enter num1:"))
            num2 = float(input("enter num2:"))
            print("result:", division(num1, num2))

        elif selection == 5:
            base = float(input("enter the base"))
            height = float(input("enter the height"))
            print("result:", calculate_triangle_area(base,height))

        elif selection == 6:
            radius = float(input("enter the radius"))
            print("result:", calculate_circle_area(radius))

        elif selection == 7:
            length = float(input("enter the length"))
            width = float(input("enter the width"))
            print("result:", calculate_rectangle_area(length,width))
        elif selection == 8:
            print("exit")
            break

main_menu()