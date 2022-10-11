# The quotient of 14 with 3 is 4 with a remainder of 2

def division(dividend: float, divisor: float) -> str:
    quotient = dividend // divisor
    rem = dividend - (quotient * divisor)
    if rem == 0:
        return f"The quotient of {dividend} and {divisor} is {quotient} with no remainder"
   
    return f"The quotient of {dividend} and {divisor} is: {quotient} and the remainder is: {rem}"

print(division(100, 3)) # The quotient of 100 and 3 is: 33 and the remainder is: 1

print(division(50, 5)) # The quotient of 50 and 5 is 10 with no remainder