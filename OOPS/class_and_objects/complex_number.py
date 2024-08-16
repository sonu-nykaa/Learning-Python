class ComplexNumber:
    def __init__(self, real, imaginary):
        self.imaginary = imaginary
        self.real = real

    def add_complex_numbers(self, number):
        real = self.real + number.real
        imaginary = self.imaginary + number.imaginary
        result = ComplexNumber(real, imaginary)
        return result

    def print_complex_number(self):
        print(self.real, " + ", self.imaginary, "i")


number1 = ComplexNumber(5, 6)
number2 = ComplexNumber(-4, 2)

result = number1.add_complex_numbers(number2)
result.print_complex_number()
