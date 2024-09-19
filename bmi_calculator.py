# BMI Calculator in Python

# Get user input for height in centimeters and weight in kilograms
height_cm = float(input("Enter your height in centimeters: "))
weight_kg = float(input("Enter your weight in kilograms: "))

# Convert height from centimeters to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight_kg / (height_m ** 2)

# Print the BMI result
print(f"Your BMI is: {bmi:.2f}")

# Determine the BMI category
if bmi <= 16:
    print("You are very underweight")
elif bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You are healthy")
elif bmi <= 30:
    print("You are overweight")
else:
    print("You are very overweight")
