import os
# Calorie Calculator

age = int(input("Enter your age in years: "))
sex = input("Enter your sex (M or F): ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

if sex == "M":
    bmr = round(66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age), 2)
elif sex == "F":
    bmr = round(655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age), 2)
else:
    print("INVALID!")

print("Your daily calorie needs are:", bmr)

# BMI Calculator

height = height / 100  # convert height from cm to m
bmi = round(weight / (height ** 2), 2)


print("Your BMI is:", bmi)

if bmi < 18.5:
    print("You are underweight.You need a Caloric Surplus.")
elif bmi < 25:
    print("You are of normal weight. You can maintain your Caloric Intake.")
elif bmi < 30:
    print("You are overweight. You need a Caloric Deficit.")
    os.system("cls")

# Calorie Intake
cal_limit = 10

while True:
    cal_intake = float(input("\nPlease enter your caloric intake for the day: "))
    diff = round(bmr - cal_intake, 2)
    os.system("cls")

    while diff > cal_limit:
        cal_intake = float(input("The calorie you need more of is {}. \n\n"
                                 "Please enter your additional caloric intake for the day: ".format(diff)))
        diff = round(diff - cal_intake, 2)

    if diff <= cal_limit:
        print("\nYou still have {} calorie for the day. But, well done!".format(diff))
    elif diff > cal_limit:
        print("\nYou have exceeded your caloric intake!")
    break
