from PIL import Image, ImageDraw


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas_path):
        # Load the image
        image = Image.open(canvas_path)

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # converting tuple of floats to integers
        int_color = tuple(round(c) for c in self.color)

        # Draw the rectangle
        draw.rectangle([self.x, self.y, self.x + self.width, self.y + self.height], fill=int_color)

        # Save or show the result
        image.save("canvas.png")
