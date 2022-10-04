# Code for a roller coaster company
# min height to get on the roller coaster company is 120cm
# Under 18 pay Ksh700 The rest pay Ksh1200



def payment_verification(name, height: float, age: int) -> str:
    if height < 120:
        print(f"Dear {name}, you have not attained the minimum height, please step down")
    elif height >= 120 and age >= 18:
        print(f"Dear {name}, welcome onboard the your ticket price is Ksh1200")
            
    else:
        print(f"Dear {name}, welcome onboard the your ticket price is Ksh1200")
    
payment_verification("Kite", 130, 19)