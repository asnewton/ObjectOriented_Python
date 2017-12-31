def gcd(num, den):
    if num > den :
        i = den
    else:
        i = num
    while(i > 0):
        if num%i == 0 and den%i == 0:
            print(i)
            break
        else:
            i = i-1

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.den, "/", self.num)

    def __add__(self, other):
        newnum = self.num*other.den + other.num*self.den
        newden = self.den*other.den
        return Fraction(newnum,newden)

def main():
    a = Fraction(2,3)
    b = Fraction(5,6)
    c = a + b
    print(a.__str__())