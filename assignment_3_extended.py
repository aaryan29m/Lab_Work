a = int(input("Enter side 1 ="))
b = int(input("Enter side 2 =")) 
c = int(input("Enter side 3 = "))

def my_function(a,b,c):
    side1 = a
    side2 = b
    side3 = c
    if side1<=0 or side1+side2==side3:
        print("not a valid triangle")
    elif side1**2+side2**2 == side3**2:
        print("right angled triangle")
    else:
        print("not a valid triangle")

my_function(a,b,c)
