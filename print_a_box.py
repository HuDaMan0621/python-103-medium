# 4. Print a Box
# Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:

# $ python3 box.py
# Width? 6
# Height? 4
# ******
# *    *
# *    *
# ******

# width = int(input('Enter width '))
# height = int(input('Enter height '))

# while(height <= width):
#     column = 1
#     while(column <= width ):
#         if(height == 1 or height == width or width == 1 or column == width):          
#             print('*', end = ' ')

width = int(input('Enter the width of the square '))
height = int(input('Enter the height of the square '))

row = 1

while(row <= height):
    column = 1
    while(column <= width ):
        if(column == 1 or column == width or row == 1 or row == height) :          
            print('*', end = ' ')
        
        else:
            print(' ', end = ' ')
        column = column + 1
    row = row + 1
    print()


#     length = int(input("Enter the side of the square  : "))

# row = 1

# while(row <= length):
#     column = 1;
#     while(column <= length ):
#         if(row == 1 or row == length or column == 1 or column == length):          
#             print('*', end = ' ')
#         else:
#             print(' ', end = ' ')
#         column = column + 1
#     row = row + 1
#     print()


# while width <= 60 and height <= 40:
#     print('*' = width * height)


#     break
# print('end')