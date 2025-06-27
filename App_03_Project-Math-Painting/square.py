from PIL import Image, ImageDraw


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas_path):
        # Load the image
        image = Image.open(canvas_path)

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # converting tuple of floats to integers
        int_color = tuple(round(c) for c in self.color)

        # Draw the square (it uses the same rectangle function but with equal sides)
        draw.rectangle([self.x, self.y, self.x + self.side, self.y + self.side], fill=int_color)

        # Save or show the result
        image.save("canvas.png")
