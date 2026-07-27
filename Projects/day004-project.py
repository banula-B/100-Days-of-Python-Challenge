#Here is a BMI calculator
#we take user input for height and weight of user

print("Enter your height in meters(ex:1.75)")
height = float(input("Enter your height in meters: "))

print("Enter your weight in kilograms(ex:70)")
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height * height)

print("Your BMI is: ", bmi)