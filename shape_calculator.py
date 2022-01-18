class Rectangle:

    def __init__(self, w, h):
        self.height = h
        self.width = w
        self.area = self.height * self.width
        self.perimeter = (2 * self.width) + (2 * self.height)
        self.diagonal = (self.width ** 2 + self.height ** 2) ** 0.5

    def get_area(self):
        return self.area

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_perimeter(self):
        return self.perimeter

    def get_diagonal(self):
        return self.diagonal

    def get_picture(self):
        pic = ""
        if self.width > 50 or self.height > 50:
            pic = "Too big for picture."
        else:
            for i in range(self.height):
                for k in range(self.width):
                    pic = pic + "*"
                pic = pic + "\n"
        return pic

    def get_amount_inside(self, shape):
        amount = round(self.height / shape.height) * round(self.width / shape.width)
        return amount

    def __str__(self):
        rect = F"Rectangle(width={self.width}, height={self.height})"
        return rect


class Square(Rectangle):

    def __init__(self, s):
        super().__init__(s, s)

    def set_side(self, s):
        self.width = s
        self.height = s

    def set_width(self, s):
        self.set_side(s)

    def set_height(self, s):
        self.set_side(s)

    def __str__(self):
        sq = F"Square(side={self.height})"
        return sq
