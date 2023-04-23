class NegativeExponentError(ValueError): 
    pass

class Calculator:
    @staticmethod
    def add(a, b):
        try:
            return a + b
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def subtract(a, b):
        try:
            return a - b
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero")
        except Exception as e:
            print(f"Error: {e}")
       

    @staticmethod
    def multiply(a, b):
        try:
            return a * b
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def exponent(a, b):
        try:
            if b < 0:
                raise NegativeExponentError("Exponent should not be negative")
            return a ** b
        except NegativeExponentError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def square_root(a):
        try:
            if a < 0:
                raise ValueError("Cannot calculate square root of a negative number")
            return a ** 0.5
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


print(Calculator.add(2, 3))
print(Calculator.subtract(5, 2))
print(Calculator.divide(10, 0))
print(Calculator.divide(10, 5))
print(Calculator.multiply(3, 4))
print(Calculator.exponent(2, 3))
print(Calculator.exponent(2, -3))
print(Calculator.square_root(-1))
print(Calculator.square_root(9))