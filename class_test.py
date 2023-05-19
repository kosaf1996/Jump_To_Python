class Calculator:
    def __init__(self, num1, num2):
        self.number1 = int(num1)
        self.number2 = int(num2)

    def add(self):
        return self.number1 + self.number2

    def sub(self ):
        return self.number1 - self.number2
    
    def mul(self):
        return self.number1 * self.number2
    
    def div(self):
        return self.number1 / self.number2
    
    def try_div(self):
        return self.number1 /self.number2