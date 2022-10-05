# Body Mass Index is a simple calculation using a person's height and weight. 
# The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in metres squared.
# A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. 
# BMI applies to most adults 18-65 years

def bmi_calculator(
    name: str, 
    age: int,
    mass_in_kg: float , 
    height_in_metres: float
    ) -> float:
    if age >= 18 and age <= 65:
        bmi = mass_in_kg/(height_in_metres**2)
        if bmi >= 25.0:
            print(f"{name} \n BMI: {round(bmi, 2)} \n  status: Overweight \n Recommendations: Exercise regularly and avoid foods high in calories \n")
        elif bmi >= 18.5 and bmi <= 24.9:
            print(f"{name} \n BMI: {round(bmi, 2)} \n  status: Healthy \n Recommendations: Congratulations, keep up with the healthy lifestyle \n")
        else: 
            print(f"Dear {name}, you bmi is below the healthy range, visit your local healthcare for more advice.\n ")
    else: 
        print(f"Dear {name}, bmi is not applicable for people in your age bracket. Check out with your local healthcare facilities for more appropriate health indicators. \n")
            
bmi_calculator("John", 35, 40, 1.1)
bmi_calculator("Jane", 18, 50, 1.5)
bmi_calculator("Joe", 56, 30, 1.6)
bmi_calculator("Jose", 70, 70, 1.3)









# command = 'Hello, World!'
# match command:
#     case 'Hello, World!':
#         print('Hello to you too!')
#     case 'Goodbye, World!':
#         print('See you later')
#     case other:
#         print('No match found')
        