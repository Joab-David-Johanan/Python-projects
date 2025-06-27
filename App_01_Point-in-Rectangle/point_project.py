from random import randint
import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, given_rectangle):
        if given_rectangle.point1.x < self.x < given_rectangle.point2.x \
                and given_rectangle.point1.y < self.y < given_rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return float((self.point2.x - self.point1.x) * (self.point2.y - self.point1.y))


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):

    def draw(self, canvas, size=10, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)

        canvas.pendown()
        canvas.dot(size, color)

        # so that you do not see the turtle cursor
        canvas.hideturtle()


rectangle = GuiRectangle(Point(randint(0, 10), randint(0, 10)), Point(randint(11, 20), randint(11, 20)))

print(
    f"Random rectangle is formed by the points: [{rectangle.point1.x},{rectangle.point1.y}]"
    f" and [{rectangle.point2.x},{rectangle.point2.y}]")

user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
print(f"The user point falls in the Rectangle:{user_point.falls_in_rectangle(rectangle)}")

user_area = float(input("Guess Area: "))
print(f"The rectangle area is {rectangle.area()} and your guess is {user_area}")
print(f"You area guess was off by {abs(rectangle.area() - user_area)}")

my_turtle = turtle.Turtle()
my_turtle.pensize(3)  # thicker lines
my_turtle.pencolor("blue")  # rectangle color

rectangle.draw(my_turtle)
user_point.draw(my_turtle)
turtle.done()
