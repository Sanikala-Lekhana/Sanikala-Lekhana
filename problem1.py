class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def calculate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"

a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter operation (add/subtract/multiply/divide): ")
calc = Calculator(a, b)
print("Result:", calc.calculate(op))
