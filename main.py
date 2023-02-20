print("\nWelcome to my BMI Calculator\n")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2

print(f"\nYour BMI is: {round(bmi)}")

if bmi < 18.5:
    print("You're Underweight")
elif bmi < 25:
    print("You're Normal Weight")
elif bmi < 30:
    print("You're Slightly Overweight")
elif bmi < 35:
    print("You're Obese")
else:
    print("You're Clinically Obese")