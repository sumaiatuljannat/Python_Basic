from traceback import print_tb

try:
    result =10/0
except ZeroDivisionError:
    print("Cannot divide by zero")


    def safe_divide(a, b):
        try:
            result = a / b
            return result

        except ZeroDivisionError:
            print("Division by zero is not allowed")

        except TypeError:
            print("Both values must be numbers")


    print(safe_divide(20, 2))

def read_data(filename):
    print("Opening file")
    try:
        f=open(filename,"r")
        data = f.read()
        print("File read successfully")
        return data
    except FileNotFoundError:
        print("File not found:",filename)
        return None
    finally:
        print("This always runs - cleanup happens here")

read_data("data.csv")

