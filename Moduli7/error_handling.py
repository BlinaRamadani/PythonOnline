#Example 1
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! Tried to divide by zero.")

#Example 2
fruits = {"apple": 5,
          "banana": 7,
          "orange": 3}

try:
    print(fruits['charry'])
except KeyError:
    print("The key does not exist in the dictionary.")

#Example 3
try:
    text_to_int = int(text)
except Exception as e:
    print("An error ocurred while pardinf data: ", e)

#Example 4, else block
try:
    result = 10/2
except ZeroDivisionError:
    print("Division by error occurred")
else:
    print("Division successful: ", result)

#Example 5
try:
    result = 10/2
except ZeroDivisionError:
    print("Division by error occurred")
finally:
    print("Finally block executed")

#Exercise
def divide_numbers(a, b):
    try:
        result = a / b
        print(("Result of division ", result))
    except ZeroDivisionError:
        print("Invalid division by zero.")
    except TypeError:
        print("Invalid type for division")
    except Exception as e:
        print(f"Unexpected error: {e}")