

print ("******AREA CALCULATOR******")
print ("""Press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle""")

choice = int(input("enter a numer between 1-4: "))
# to area calculator



if choice == 1:
    side = float(input("enter the length of one side: "))
    area = side**2
    print("the area of square is ", area)

elif choice == 2:
    length = float(input("enter the length of the rectangle: "))
    weidth = float(input("enter the weidth of the rectangle: "))
    area = length*weidth
    print ("the area of rectangle is ", area)

elif choice == 3:
    radius = float(input("enter the radius of the circle: "))
    area = ((22/7)*(radius**2))
    print("the area of the circle is", area)

elif choice ==4:
    base = float(input("enter the base of the triangle: "))
    hight = float(input("enter the hight of the triangle: "))
    area = 0.5*base*hight
    print("the area of the triangle is", area)
