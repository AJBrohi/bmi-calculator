print("Welcome to my BMI Calculator\n")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / (float(height) * float(height))

print(int(bmi))