# print(len(input("name")) + "samad")

# no = input("type in a year:  \n")
# first = int(no[0])
# secong = int(no[1])
# print(first + secong)

# x = kg/m2
##############################################
# weight = float(input("enter your weight:  \n"))
# height = float(input("enter your height:  \n"))
# Bmi = round(weight / height ** 2)
# if Bmi < 18.5:
#     print(f"Your BMI is {Bmi}, you are underweight.")
# elif Bmi > 18.5 and Bmi < 25:
#     print(f"Your BMI is {Bmi}, you have a normal weight.")
# elif Bmi > 25 and Bmi < 30:
#     print(f"Your BMI is {Bmi}, you are slightly overweight.")
# elif Bmi > 30 and Bmi < 35:
#     print(f"Your BMI is {Bmi}, you are obese.")
# elif Bmi > 35:
#     print(f"Your BMI is {Bmi}, you are clinically obese.")
####################################################
# rod = round(4/3, 3)

# print(f"the answer is {rod}")
# print("Wecome to the tip calculator")
# total = float(input("What it the total bill? "))
# tip = float(
#     input("what percentage tip would you like to give? 10, 12, or 15? %"))
# no_of_people = float(input("How many people to split the bill? "))
# tper = tip/100
# tper += 1
# # print(tper)
# # print(round(split, 2))
# if no_of_people < 10:
#     split = (total / no_of_people) * tper
#     print("{:.2f}".format(split))
# elif tip > 100:
#     request = input(f"Are you sure u wannt to continue to us ${tip}")
#     if request == "yes" and no_of_people < 10:
#         split = (total / no_of_people) * tper
#         print("{:.2f}".format(split))
#     elif request == "yes" and no_of_people > 10:
#         print("No of people greater than 10, transaction declined")
#     elif request == "no":
#         print('restart calculation')

# elif no_of_people > 10:
#     print("No of people greater than 10, transaction declined")
# else:
#     print('noting is being done')


########################################
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# Unless the year is also evenly divisible by 400
# 2000 / 4=500 (leap)
# 2000/ 100= 20 (not leap)
# 2000/ 4000= 5 (leap)
# year = int(input("The year you want to check: \n"))

# first method
# if year % 4 == 0 and year % 4 == 0 and year % 4 == 0:
#     print("is leap")
# else:
#     print("not leap")
# method 2
# if year % 4 == 0:
#     if year % 4 == 0:
#         if year % 4 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")

# print("welcome to our rollercoster")
# height = int(input("what's your height in cm? "))
# bill = 0
# if height >= 120:
#     print("you can ride the roller coster :D")
#     age = int(input("what's your age ?"))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age <= 18:
#         bill = 7
#         print("youth tickets are $7")
#     else:
#         bill = 12
#         print("adult tickets are $12")
#     Want_photo = input("Do u want a picture on your ride?  Y or N")
#     upper = Want_photo.upper()

#     if upper == "Y":
#         # add $3 to the initial bill
#         bill += 3
#         print(f"your bill is {bill}")

# else:
#     print("You have to grow taller to ride.")

######################################
# print("Welcome to python pizza Deliveries")
# size = input("What size pizza do you want ? S , M or L \n").upper()
# price = 0
# if size == "S":
#     price = 15
# elif size == "M":
#     price = 20
# elif size == "L":
#     price = 25
# else:
#     print("Not available")

# extra_cheese = input("Do you want cheese or not ? Y or N \n").upper()
# if extra_cheese == "Y":
#     price += 1
# else:
#     price += 0

# add_pepperoni = input("Do you want pepperoni or not ? Y or N \n").upper()
# if add_pepperoni == "Y":
#     if size == "S":
#         price += 2
#     elif size == "M" or size == "L":
#         price += 3
# else:
#     price += 0

# print("$" + str(price))

######################################
# print("welcome to love calculator")
# user = input("Please input your name: \n").lower()
# user_2 = input("Your crush's name: \n").lower()

# # true
# t = user.count("t")
# r = user.count("r")
# u = user.count("u")
# e = user.count("e")

# t2 = user_2.count("t")
# r2 = user_2.count("r")
# u2 = user_2.count("u")
# e2 = user_2.count("e")

# # love
# l = user.count("l")
# o = user.count("o")
# v = user.count("v")
# e = user.count("e")

# l2 = user_2.count("l")
# o2 = user_2.count("o")
# v2 = user_2.count("v")
# e2 = user_2.count("e")

# A = t + r + u + e
# A2 = l + o + v + e
# # print(A)
# # print(A2)
# B = t2 + r2 + u2 + e2
# B2 = l2 + o2 + v2 + e2
# # print(B)
# # print(B2)
# C = A + B
# C2 = A2 + B2
# score = str(C) + str(C2)
# print(f"the score is {score}")

# if int(score) < 10 or int(score) > 90:
#     print(f"your score is {score}, you o together like coke and mentos")
# elif int(score) > 40 or int(score) < 60:
#     print(f"your score is {score}, you are alright together")

######################################
"""functions ouput"""

# first = int(input("input a year: \n"))
# sec = int(input("input a sec year: \n"))
# third = int(input("input a third year: \n"))
# first_list = [first, sec, third]
# check = input("which would u like to check first? \n")
# upper_2 = check.upper()

# checker = first
# if check == "A":
#     checker = first
# elif check == "B":
#     checker = sec
# elif check == "C":
#     checker = third

# if checker % 4 == 0:
#     if checker % 4 == 0:
#         if checker % 4 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")

# cont = input("Would u like to check the rest? Y or N")
# confirmation = cont.upper()

# if confirmation == "Y":


# print("Welcome to treasure hunt🗝️  😂")

# row_1 = ["🟧", "🟧", "🟧"]
# row_2 = ["🟧", "🟧", "🟧"]
# row_3 = ["🟧", "🟧", "🟧"]
# print(f"{row_1}\n{row_2}\n{row_3}")
# # maps = [row_1, row]
# user_input = input("chose your pick : \n")
# if len(user_input) > 2:
#     print("location not found")
# elif user_input == "23":
#     row_1[2] = " X"
#     print(f"You found the treasure..yay😂 \n{row_1}\n{row_2}\n{row_3}")
# else:
#     print("You just died 💀 .")
"""method 2"""
# row1 = ["🟧", "🟧", "🟧"]
# row2 = ["🟧", "🟧", "🟧"]
# row3 = ["🟧", "🟧", "🟧"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("where do u want to put it ?")
# #25
# horizontal = int(position[0])#The first input number
# vertical = int(position[1])#The Second input number

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"
"""method 3"""
# row1 = ["🟧", "🟧", "🟧"]
# row2 = ["🟧", "🟧", "🟧"]
# row3 = ["🟧", "🟧", "🟧"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("where do u want to put it ?")
# #25
# horizontal = int(position[0])#The first input number
# vertical = int(position[1])#The Second input number

# map[vertical - 1][horizontal - 1] = "X"
#
"""end of code"""
# print(f"{row1}\n{row2}\n{row3}")
#      1     2      3
# 1 ["🟧", "🟧", "🟧"]
# 2 ["🟧", "🟧", "🟧"]
# 3 ["🟧", "🟧", "🟧"]
"""additional note"""
# list1 = [23, 34, 12]
# list2 = [19, 234, 62]
# list3 = [29, 48, 10]

# m = [list1, list2, list3]

# print(m[1][1])

"""for loops"""
# list1 = [23, 34, 12]

# for numbers in list1:
#     if numbers > 30:
#         print("X")
#     else:
#         print("Y")

#############################
# student = input("Give the students heights: \n").split()
# # split function convert strings to lists
# for i in range(0, len(student)):
#     student[i] = int(student[i])
# print(student)

# total_height = 0
# for intergers in student:
#     total_height += intergers
# print(total_height)

# no_of_stud = 0
# for stud in student:
#     no_of_stud += 1

# average = total_height / no_of_stud
# print(average)


scores = input("put the scores here : \n").split()

for i in range(0, len(scores)):
    scores[i] = int(scores[i])
print(scores)

heighest = 0
for n in scores:
    if n > heighest:
        heighest = n
print(heighest)
