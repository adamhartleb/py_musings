class FieldElement():
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = f'Num {num} not in field range 0 to {num}'
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return f'FieldElement_{self.prime}({self.num})'

    def __eq__(self, value):
        if value is None:
            return False
        return self.num == value.num and self.prime == value.prime

    def __ne__(self, value):
        if value is None:
            return True
        return self.num != value.num or self.prime != value.prime

    def __add__(self, value):
        if self.prime != value.prime:
            raise TypeError('Cannot add two numbers in different fields.')
        num = (self.num + value.num) % self.prime
        return self.__class__(num, self.prime)


a = FieldElement(6, 13)
b = FieldElement(10, 13)

print(a + b)
