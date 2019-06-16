# This program outputs a downwards facing half arrow composed of a rectangle and a right triangle.
# The arrow dimensions are defined by user specified 
# arrow base height, arrow base width, and arrow head width.

# Function Definitions
# Three funcitons are defined.
# Draw the base of the arrow.
# Draw the head of the arrow.
# Draw the half arrow.
# Separate definitions are defined for clarity.
# Each function serves a separate, single purpose .
# For loops are used for drawing as the parameters dictate the number of iterations.

def draw_base(height:int, width:int) -> str:
    '''
    Print ASCII Art for the arrow base

    Keyword arguments:
    height -- an int representing the desired height
    width -- an int representing the desired width
    '''
    # Draw arrow base (height = base_height, width = base_width).
    for i in range(height):
        print('*'*width)

def draw_head(head_width:int) -> str:
    '''
    Print ASCII Art for the arrow head

    Keyword arguments:
    head_width -- an int representing the desired head width
    '''
    # Draw arrow head (head_width = largest width at head base).
    for i in reversed(range(1, head_width + 1)):
        print('*'*i)

def draw_arrow(height:int, width:int, head_width:int) -> str:
    '''
    Print ASCII Art for the full half arrow

    Keyword arguments:
    height -- an int representing the desired height
    width -- an int representing the desired width
    head_width -- an int representing the desired head width
    '''
    # Draw half arrow (arrow base + arrow head).
    draw_base(height, width)    
    draw_head(head_width)

# Only execute if this is the main script run 
# and script is not imported by another module
if __name__ == "__main__":
    # Grab user defined dimenstions and assign them to variables.
    # These variables will serve as arguments for specific instances
    # of the functions defined above.

    # Converting the string intput into int data types is needed for function iteration.
    # The loops defined in the functions will not iterate over strings or floats as currently defined.

    base_height = int(input('Enter arrow base height: \n'))
    base_width = int(input('Enter arrow base width: \n'))
    head_width = int(input('Enter arrow head width: \n'))

    # A while loop is used to collect input to ensure the
    # head width is greater than base width to ensure arrow shape.
    # A while loop is used because the number of iterations is unknown.

    while (head_width <= base_width):
        head_width = int(input('Head width must be greater than base width\nEnter arrow head width: \n'))

    draw_arrow(base_height, base_width, head_width)