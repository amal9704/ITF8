name = input("enter your full name:")
num = input("enter your mobile number as 05x-xxxx-xxx:")
year_of_birth = input("enter your year of birth:")
year_of_birth = int(year_of_birth)
current_year = 2023
user_age = current_year - year_of_birth
print(name)
print(user_age)
print(num.split("-"))