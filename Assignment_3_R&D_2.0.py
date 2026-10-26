a = int(input("enter side1 = "))
b = int(input("enter side2 = "))
c = int(input("enter side3 = "))

def my_function(a, b, c):
    side1 = a
    side2 = b
    side3 = c

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("not a valid triangle")
    elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1: 
        print("not a valid triangle")

    elif side1 == side2 == side3:
        print("equilateral triangle")

    elif (side1**2 + side2**2 == side3**2 or
          side1**2 + side3**2 == side2**2 or
          side2**2 + side3**2 == side1**2):
        print("right angled triangle")

    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("isosceles triangle")

    else:
        print("scalene triangle")

my_function(a, b, c)
