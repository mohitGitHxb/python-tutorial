import turtle
import random
import math

# 1. Basic Turtle Drawing
def basic_shapes():
    # Create a turtle screen
    screen = turtle.Screen()
    screen.title("Basic Shapes")
    
    # Create turtle object
    t = turtle.Turtle()
    t.speed(2)  # Drawing speed
    
    # Draw a square
    for _ in range(4):
        t.forward(100)
        t.right(90)
    
    # Move to new position
    t.penup()
    t.goto(200, 0)
    t.pendown()
    
    # Draw a circle
    t.circle(50)
    
    screen.mainloop()

# 2. Colorful Spiral
def colorful_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.width(2)
    
    colors = ["red", "purple", "blue", "green", "orange", "yellow"]
    
    for x in range(360):
        t.pencolor(colors[x % 6])
        t.forward(x * 0.5)
        t.left(59)
    
    screen.mainloop()

# 3. Fractal Tree
def fractal_tree(t, branch_length, angle):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(angle)
        
        fractal_tree(t, branch_length - 15, angle)
        
        t.left(angle * 2)
        
        fractal_tree(t, branch_length - 15, angle)
        
        t.right(angle)
        t.backward(branch_length)

def draw_fractal_tree():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.left(90)
    t.speed(0)
    t.color("green")
    
    fractal_tree(t, 100, 30)
    
    screen.mainloop()

# 4. Interactive Drawing Game
def interactive_drawing():
    screen = turtle.Screen()
    screen.setup(600, 400)
    screen.title("Interactive Drawing")
    
    # Drawing turtle
    t = turtle.Turtle()
    t.speed(0)
    
    # Color change function
    def change_color():
        t.pencolor(random.random(), random.random(), random.random())
    
    # Movement functions
    def move_forward():
        t.forward(50)
    
    def move_backward():
        t.backward(50)
    
    def turn_right():
        t.right(45)
    
    def turn_left():
        t.left(45)
    
    def clear_screen():
        t.clear()
        t.penup()
        t.home()
        t.pendown()
    
    # Keyboard bindings
    screen.onkey(move_forward, "Up")
    screen.onkey(move_backward, "Down")
    screen.onkey(turn_right, "Right")
    screen.onkey(turn_left, "Left")
    screen.onkey(change_color, "c")
    screen.onkey(clear_screen, "x")
    
    screen.listen()
    screen.mainloop()

# 5. Mandala Art Generator
def mandala_art():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    
    colors = ["red", "blue", "green", "purple", "orange"]
    
    for i in range(36):
        t.pencolor(colors[i % len(colors)])
        
        # Draw star-like pattern
        for _ in range(5):
            t.forward(200)
            t.right(144)
        
        t.right(10)
    
    screen.mainloop()

# 6. Animated Polygon Generator
def animated_polygons():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.title("Animated Polygons")
    
    t = turtle.Turtle()
    t.speed(2)
    
    def draw_polygon(sides, size):
        angle = 360 / sides
        for _ in range(sides):
            t.forward(size)
            t.right(angle)
    
    # Draw multiple polygons
    polygon_sizes = [50, 100, 150, 200]
    polygon_sides = [3, 4, 5, 6, 8]
    
    for size in polygon_sizes:
        for sides in polygon_sides:
            t.pencolor(random.random(), random.random(), random.random())
            draw_polygon(sides, size)
            t.penup()
            t.forward(size * 2)
            t.pendown()
    
    screen.mainloop()

# 7. Advanced Parametric Art
def parametric_art():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    
    # Parametric equation art
    for theta in range(0, 720, 5):
        r = theta * 0.5
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        
        t.pencolor(abs(math.sin(theta/100)), 
                   abs(math.cos(theta/50)), 
                   abs(math.tan(theta/75)))
        
        t.goto(x, y)
    
    screen.mainloop()

# Main execution
def main():
    print("Turtle Graphics Menu:")
    print("1. Basic Shapes")
    print("2. Colorful Spiral")
    print("3. Fractal Tree")
    print("4. Interactive Drawing")
    print("5. Mandala Art")
    print("6. Animated Polygons")
    print("7. Parametric Art")
    
    choice = input("Enter your choice (1-7): ")
    
    options = {
        '1': basic_shapes,
        '2': colorful_spiral,
        '3': draw_fractal_tree,
        '4': interactive_drawing,
        '5': mandala_art,
        '6': animated_polygons,
        '7': parametric_art
    }
    
    selected_function = options.get(choice)
    if selected_function:
        selected_function()
    else:
        print("Invalid choice!")

# Run the main program
if __name__ == "__main__":
    main()