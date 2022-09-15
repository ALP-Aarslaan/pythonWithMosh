class Points:
    x = 0
    y = 0

    def draw(self):
        print("draw point")

    def move(self):
        print("move point")


point1 = Points()
point1.y = 20
point1.x = 22
print(point1.x, point1.y)
point1.move()
point1.draw()
