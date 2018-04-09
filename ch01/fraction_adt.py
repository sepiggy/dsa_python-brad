class Fraction(object):

    def __init__(self, top, bottom):
        if not (isinstance(top, int) and isinstance(bottom, int)):
            raise RuntimeError(
                'the numerator and denominator should be integer.')
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den
        return Fraction(newnum, newden)

    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den*other.den
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


myf = Fraction(3, 5)
print(myf)
print('I ate', myf, 'of the pizza')

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1+f2
print("Add:", f3)

f4 = Fraction(7, 12)
f5 = Fraction(7, 12)
print(f4 == f5)

f14 = Fraction(2, 9)
f15 = Fraction(2, 9)
print("<=:", f14 <= f15)

f6 = Fraction(3, 4)
f7 = Fraction(1, 2)
print("Sub:", f6 - f7)

f8 = Fraction(4, 7)
f9 = Fraction(3, 8)
print(f8 * f9)

f10 = Fraction(3, 8)
f11 = Fraction(1, 2)
print(f10 / f11)

f12 = Fraction(1, 3)
f13 = Fraction(1, 5)
print(f13 < f12)

Fraction(-3.5, 4)
