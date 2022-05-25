class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    def gcd(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def lcm(self, a, b):
        # 12 6 = 4
        # 3*4*4 = 48
        x = self.gcd(a, b)
        return a * b / x

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        denominator = self.lcm(b, d)
        nominator = a * (denominator / b) + c * (denominator / d)
        return Fraction(nominator, denominator)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)


# f = Fraction(30, 16)
# print(f)

a = Fraction(1, 3)
b = Fraction(1, 2)
print(a+b)