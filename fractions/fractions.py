# Calculate the greatest common divisor (aka greatest common factor)
# of two numbers
#
# See https://en.wikipedia.org/wiki/Euclidean_algorithm
def gcd(a, b):
    return 1 # Change

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return f"?/?"

    # Calculate the value of the fraction as a single number
    def value(self):
        pass

    def __mul__(self, other):
        return Fraction(1, 1) # Change

    def __add__(self, other):
        return Fraction(1, 1) # Change

a = Fraction(1, 2)

print(a)                    # 1/2
print(a.value())            # 0.5
print(a + Fraction(10, 25)) # 9/10
print(a * Fraction(10, 25)) # 1/5
