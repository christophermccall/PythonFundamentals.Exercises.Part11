class Rectangle:
    width = 0
    length = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        if self.width is None:
            x = self.length * self.length
        else:
            x = self.width * self.length

        return x

    def perimeter(self):
        if self.width is None:
            x = self.length * 4
        else:
            x = (self.width + self.length) * 2
        return x


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, None)

