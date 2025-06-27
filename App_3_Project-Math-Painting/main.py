import numpy as np
from PIL import Image

from rectangle import Rectangle
from square import Square


class Canvas:
    def __init__(self):
        self.width = None
        self.height = None
        self.color = None

    def create_canvas(self):
        canvas_dimensions = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        if self.color == "white":
            canvas_dimensions[:] = [255, 255, 255]
        elif self.color == "black":
            canvas_dimensions[:] = [0, 0, 0]

        img = Image.fromarray(canvas_dimensions, 'RGB')
        img.save("canvas.png")


# canvas creation
canvas_obj = Canvas()
canvas_obj.width = int(input("Enter the width of the canvas: "))
canvas_obj.height = int(input("Enter the height of the canvas: "))
canvas_obj.color = input("Enter the color of the canvas: e.g. white or black ")
canvas_obj.create_canvas()

while True:
    # user drawing options
    user_input = input("Enter what you want to draw, if nothing the type 'quit': ")

    match user_input:
        case "rectangle":
            # rectangle creation
            start_x_rec = float(input("Enter the starting x-point for the rectangle: "))
            start_y_rec = float(input("Enter the ending y-point for the rectangle: "))
            rec_width = float(input("Enter the width of the rectangle: "))
            rec_height = float(input("Enter the height of the rectangle: "))
            rec_color_r = float(input("Enter amount of red you want for the rectangle: "))
            rec_color_g = float(input("Enter amount of green you want for the rectangle: "))
            rec_color_b = float(input("Enter amount of blue you want for the rectangle: "))

            rec_obj = Rectangle(start_x_rec, start_y_rec, rec_width, rec_height,
                                (rec_color_r, rec_color_g, rec_color_b))
            rec_obj.draw(canvas_path=r"C:\Python_Projects\App-3-Project-Math-Painting\canvas.png")

        case "square":
            # square creation
            start_x_square = float(input("Enter the starting x-point for the square: "))
            start_y_square = float(input("Enter the ending y-point for the square: "))
            square_side = float(input("Enter the dimension of the square: "))
            square_color_r = float(input("Enter amount of red you want for the square: "))
            square_color_g = float(input("Enter amount of green you want for the square: "))
            square_color_b = float(input("Enter amount of blue you want for the square: "))

            square_obj = Square(start_x_square, start_y_square, square_side,
                                (square_color_r, square_color_g, square_color_b))
            square_obj.draw(canvas_path=r"C:\Python_Projects\App-3-Project-Math-Painting\canvas.png")

        case "quit":
            print("Exiting application...")
            # exit the application
            break

        case _:
            print("Invalid input! Try again")
