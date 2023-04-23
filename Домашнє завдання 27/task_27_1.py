class NegativeExponentError(ValueError): 
    pass

class Calculator:
    def __init__(self, value = 0):
        self.value = value
   
    def add(self, other):
        try:
            self.value += other
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print(self.value)

   
    def subtract(self, other):
        try:
            self.value -= other
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print(self.value)

   
    def divide(self, other):
        try:
            self.value /= other
        except ZeroDivisionError:
            print("Error: Division by zero")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print(self.value)
   
    def multiply(self, other):
        try:
            self.value *= other
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print(self.value)

   
    def exponent(self, other):
        try:
            if other < 0:
                raise NegativeExponentError("Exponent should not be negative")
            self.value = self.value ** other
        except NegativeExponentError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print(self.value)
   
    def square_root(self):
        try:
            if self.value < 0:
                raise ValueError("Cannot calculate square root of a negative number")
            self.value = self.value ** 0.5
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print(self.value)

calculator = Calculator(2)
calculator.add(3)
calculator.subtract(2)
calculator.divide(0)
calculator.multiply(4)
calculator.exponent(2)
calculator.exponent(-3)
calculator.square_root()
calculator.multiply(-1)
calculator.square_root()
