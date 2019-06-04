# This program outputs a downwards facing arrow composed of a rectangle and a right triangle. 
# The arrow dimensions are defined by user specified 
# arrow base height, arrow base width, and arrow head width.

# Function Definitions


# Grab and user defined dimenstions and assign them to reusable variables
# Converting the string intput into int data types is best here for later iteration
# The loops defined in the functions will not be able to iterate 
# over strings or floats as currently defined

base_height = int(input('Enter arrow base height: \n'))
base_width = int(input('Enter arrow base width: \n'))
head_width = int(input('Enter arrow head width: \n'))

while (head_width <= base_width):
    head_width = int(input('Enter arrow head width: \n'))
# Draw arrow base (height = base_height, width = base_width)
# Nested for loops used here; we know the number of iterations ahead of time
for i in range(base_height):
    print('*'*base_width)
for i in reversed(range(1, head_width + 1)):
    print('*'*i)