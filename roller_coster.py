# Code for a roller coaster company
# min height to get on the roller coaster company is 120cm
# Under 18 pay Ksh700 The rest pay Ksh1200


def payment_verification(name: str, height_in_cm: float, age_in_yrs: int) -> str:
    if height_in_cm < 120:
        print(f"Dear {name}, you have not attained the minimum height, please step down")
    elif height_in_cm >= 120 and age_in_yrs >= 18:
        print(f"Dear {name}, welcome onboard the your ticket price is Ksh1200")    
    else:
        print(f"Dear {name}, welcome onboard the your ticket price is Ksh1200")

payment_verification("Kite", 130, 19)