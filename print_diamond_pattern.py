
'''
write a function that prints a diamond shape using asterisks("*"). the diamond shape consists of an upper pyramid (including
the middle line) and a lower inverted pyramid.
'''

def diamond(rows):
    for i in range(1, rows + 1): #This loop runs from 1 to rows inclusive.

        print(" " *(rows - i) + "*" * (2 * i -1))
    for i in range(rows -1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

diamond(5)

# alternative

def print_row(spaces, stars):
    print(" " * spaces + "*" * stars)

def diamond(rows):
    # Upper pyramid
    for i in range(rows):
        print_row(rows - i - 1, 2 * i + 1)
    # Lower inverted pyramid
    for i in range(rows - 2, -1, -1):
        print_row(rows - i - 1, 2 * i + 1)

diamond(5)
