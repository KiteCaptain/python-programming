# The quotient of 14 with 3 is 4 with a remainder of 2

def division(dividend, divisor):
    quotient = dividend // divisor
    rem = dividend - (quotient * divisor)
    if rem == 0:
        return f"The quotient of {dividend} and {divisor} is {quotient} with no remainder"
   
    return f"The quotient of {dividend} and {divisor} is: {quotient} and the remainder is: {rem}"

print(division(20, 3)) # The quotient of 20 and 3 is: 6 and the remainder is: 2
print(division(20, 4)) # The quotient of 20 and 4 is 5 with no remainder