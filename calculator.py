class Calculator:

    def __init__(self, value1, value2):
        self.value1 = float(value1)
        self.value2 = float(value2)

    # Adder function
    def adder(self):
        return self.value1 + self.value2

    # Subtractor function
    def subtractor(self):
        return self.value1 - self.value2

    # Multiplication function
    def multiplier(self):
        return self.value1 * self.value2

    # Divider function
    def divider(self):
        return self.value1/self.value2

    # Clear function
    def clear(self):
        self.value1 = self.value2 = 0


input1 = input("Enter your first input: ")
input2 = input("Enter your second input: ")
calculator = Calculator(input1, input2)


print("Addition: ", calculator.adder())
print("Subtraction: ", calculator.subtractor())
print("Multiplication: ", calculator.multiplier())
print("Division: ", calculator.divider())
print("Clear: ", calculator.clear())
