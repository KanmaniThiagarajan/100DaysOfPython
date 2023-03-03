class DrawShape:
    def __init__(self, shape, sides, color):
        self.shape = shape
        self.sides = sides
        self.color = color

    def draw(self, timmy):
        angle = round(int(360 / self.sides))
        for i in range(0, self.sides):
            timmy.color(self.color)
            timmy.forward(100)
            timmy.right(angle)

