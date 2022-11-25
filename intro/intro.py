# print(len(input("name")) + "samad")

# no = input("type in a number:  \n")
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

print("welcome to our rollercoster")
height = int(input("what's your height in cm? "))
if height >= 120:
    print("you can ride the roller coster :D")
    age = int(input("what's your age ?"))
    if age < 12:
        print("Child tickets are $5")
    elif age >= 18:
        print("youth tickets are $7")
    else:
        print("adult tickets are $12")
