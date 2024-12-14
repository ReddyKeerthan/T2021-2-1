#Small Calculator

class Calculator:
    def calculate(self, n1, n2, opt):
        if opt == "Addition":
            return n1 + n2
        elif opt == "Subtraction":
            return n1 - n2
        elif opt == "Multiplication":
            return n1 * n2
        elif opt == "Division":
            if n2 != 0:
                return n1 / n2
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

# Example usage
calc = Calculator()
result = calc.calculate(10, 5, "Addition")
print("Result:", result)