class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return ("Rectangle(width=%i, height=%i)" % (self.width, self.height))

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if any(side > 50 for side in [self.width, self.height]):
            return "Too big for picture."
        else:
            lines = []
            line = ("*" * self.width) + "\n"

            i = 0
            while True:
                lines.append(line)
                i += 1
                if i >= self.height:
                    break

            return "".join(lines)

    def get_amount_inside(self, shape):
        on_width = int(self.width / shape.width)
        on_height = int(self.height / shape.height)

        return on_width * on_height


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return ("Square(side=%i)" % (self.width))

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)
