
# def factorial(n):
#    result = 1
#   for i in range(1, n + 1):
#      result *= i
#   return result

# number = int(input("Enter a number: "))
# fact = factorial(number)
# print("The factorial of", number, "is", fact)

#if __name__ == '__main__':
#    n = int(input("enter the number"))
#    for i in range(0,21):
#       if i < n:
#            print (i**2)

year = int(input("enter the year"))
def is_leap(year):
        if year % 4 == 0:
             return True
        else :
            print(False)
is_leap(1994)