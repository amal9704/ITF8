with open('my file',"a") as file:
    user_name = input("enter your name")
    user_age = input("enter your age")
    user_birthday = input("enter your birthday")
    file.write(user_name+"\t")
    file.write(user_age+"\t")
    file.write(user_birthday)
    file.close()

