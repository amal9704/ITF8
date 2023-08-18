def check_num():
    selection = int(input("1. for palindrome check, 2. for even/odd check 3.exit: "))


    if selection == 1:
        num = input("Enter a numb: ")
        if num == num[::-1]:
            print("The number is a palindrome")
        else:
            print("The number is not a palindrome")

    elif selection == 2:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")

    elif selection == 3:
        print("exit")

    else:
        print("Invalid choice. Please try again.")


check_num()

def find_smallest_largest(numbers):
    numbers.sort()
    smallest = numbers[0]
    largest = numbers[-1]
    return smallest, largest
num_list = [3,6,7,9]
smallest_num, largest_num = find_smallest_largest(num_list)
print("Smallest number:", smallest_num)
print("Largest number:", largest_num)


