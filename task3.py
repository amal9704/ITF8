def triangle():
    height = int(input("enter the heigh:t"))
    base = int(input(" enter the base"))
    area = 0.5 * height * base
    print(area)

    if area >= 10:
          print("area is big")
    elif area < 10 :
         print(("area is small"))
    elif area <= 0 :
         print("invaild input")


triangle()

def sguare():
    y = int(input("enter the length"))
    area = y * y
    print(area)
    if area >= 10:
            print("area is big")
    elif area < 10 :
            print(("area is small"))
    elif area <= 0 :
            print("invaild input")
sguare()

def circle():
    r = int(input("enter the radius"))
    area = r ** 2 *3.24
    print(area)
    if area >= 10:
          print("area is big")
    elif area < 10 :
         print(("area is small"))
    elif area <= 0 :
         print("invaild input")


