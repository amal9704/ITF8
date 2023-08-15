def calculate_avarege(marks):
    avarage = sum(marks) / len(marks)
    return avarage

stu_num = int(input("enter the number of students:"))

for i in range(stu_num):
    mark_num = int(input(f'enter the number of marks:'))
    marks = []
    for j in range(mark_num):
        mark = float(input(f"enter mark{j+1} for student{i+1}:"))
        marks.append(mark)


    print(marks)
    print("avarege = ",calculate_avarege(marks))
    print("max mark = ",max(marks))
    print("min mark = ",min(marks))