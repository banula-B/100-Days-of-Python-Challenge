#Here is a BMI calculator
#we take user input for height and weight of user

print("Enter your height in meters(ex:1.75)")
height = float(input("Enter your height in meters: "))

print("Enter your weight in kilograms(ex:70)")
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height * height)

print("Your BMI is: ", bmi)

'''
Underweight: Less than 18.5
Healthy Weight: 18.5 to 24.9
Overweight: 25.0 to 29.9
Obesity (Class 1): 30.0 to 34.9
Obesity (Class 2): 35.0 to 39.9
Severe Obesity (Class 3): 40.0 or greater
'''

if bmi<18.5:
    print("You are underweighted!")
elif bmi<24.9:
    print("You are healthy!")
elif bmi<29.9:
    print("You are overweight!")
elif bmi<34.9:
    print("You are obese (Class 1)!")
elif bmi<39.9:
    print("You are obese (Class 2)!")
else:
    print("You are severely obese (Class 3)!")