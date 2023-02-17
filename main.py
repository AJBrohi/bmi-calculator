print("\nWelcome to my BMI Calculator\n")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2

print(f"\nYour BMI is: {round(bmi)}")

if bmi < 18.5:
    print("You're Underweight")

elif bmi < 25:
    print("You're Normal Weight")
    
elif bmi < 30:
    print("You're Overweight")
    
else:
    print("You're Obese")