from math import gcd
class Rational:

    def __init__(self, numerator, denominator):
        self.check(numerator, denominator)
        self.__numerator, self.__denominator = self.simple_form(numerator, denominator)

    def getFraction(self):
        return f'{self.__numerator} / {self.__denominator}'

    def getFloating(self):
        return self.__numerator / self.__denominator

    def check(self, numer, denom):
        if not (isinstance(numer, int) and isinstance(denom, int)):
            raise TypeError("Wrong value type")
        if not denom:
            raise ZeroDivisionError

    def add(self, newnum: int, newdenom: int):
        self.check(newnum, newdenom)
        self.__numerator, self.__denominator = self.simple_form(
            self.__numerator * newdenom + newnum * self.__denominator,
            self.__denominator * newdenom)

    def sub(self, newnum: int, newdenom: int):
        self.check(newnum, newdenom)
        self.__numerator, self.__denominator = self.simple_form(
            self.__numerator * newdenom - newnum * self.__denominator, self.__denominator * newdenom)

    def mult(self, newnum: int, newdenom: int):
        self.check(newnum, newdenom)
        self.__numerator, self.__denominator = self.simple_form(self.__numerator * newnum,
                                                                 self.__denominator * newdenom)

    def div(self, newnum: int, newdenom: int):
        self.mult(newdenom, newnum)

    def simple_form(self, numer, denom):
        k = gcd(numer, denom)
        return numer // k, denom // k


x = Rational(input("Enter first argument"), input("Enter second argument"))

print(x.getFloating())
print(x.getFraction())

x.add(4, 5)

print(x.getFloating())
print(x.getFraction())

x.sub(1, 2)

print(x.getFloating())
print(x.getFraction())

x.div(4, 5)

print(x.getFloating())
print(x.getFraction())

x.sub(1, 0)

print(x.getFloating())
print(x.getFraction())
