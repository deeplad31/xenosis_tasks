import turtle

# Initialize the turtle
screen = turtle.Screen()
pen = turtle.Turtle()

# Function to draw a square
def draw_square(size, color):
    pen.color(color)
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

# Function to draw a triangle
def draw_triangle(size, color):
    pen.color(color)
    for _ in range(3):
        pen.forward(size)
        pen.left(120)

# Function to draw a circle
def draw_circle(radius, color):
    pen.color(color)
    pen.circle(radius)

# Function to clear the drawing
def clear_drawing():
    pen.clear()

# Main function to take user inputs and draw shapes
def main():
    while True:
        shape = screen.textinput("Shape", "Enter shape to draw (square, triangle, circle) or 'clear' to start over:").lower()
        
        if shape == 'clear':
            clear_drawing()
            continue
        
        size = int(screen.textinput("Size", "Enter the size of the shape:"))
        color = screen.textinput("Color", "Enter the color of the shape:")

        if shape == 'square':
            draw_square(size, color)
        elif shape == 'triangle':
            draw_triangle(size, color)
        elif shape == 'circle':
            draw_circle(size, color)
        else:
            print("Invalid shape. Please enter 'square', 'triangle', or 'circle'.")

        another = screen.textinput("Another", "Do you want to draw another shape? (yes/no):").lower()
        if another != 'yes':
            break

    screen.bye()

# Run the program
main()
