def divide(a, b):
    return a / b

# ZeroDivisionError and TypeError
try:
    divide(20, 10)
except ZeroDivisionError as ex:
    print('Error!', ex)
except TypeError as ex:
    print( 'something went wrong again!', ex)
except Exception as ex:
    print(ex)


# FileNotFoundError
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as ex:
    print(ex)


# IndexError
items = [1,2,3,4,5]
try: 
    item = items[6]
    print(item)
except IndexError as ex:
    print(ex)