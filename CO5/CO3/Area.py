from Graphics.RectFunctions import*
from Graphics.CirFunctions import*
from Graphics.Dgraphics.CuboidFunctions import*
from Graphics.Dgraphics.SphereFunctions import*
#rectangle
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle Perimeter=",RectPerimeter(l,b))
#Circle
r=int(input("Enter radius of Circle:"))
print("Circle Area=",CirArea(r))
print("Circle Perimeter=",CirPerimeter(r))
#Cuboid
l=int(input("Enter Cuboid length:"))
b=int(input("Enter Cuboid breadth:"))
h=int(input("Enter Cuboid height:"))
print("Cuboid Area=",CubArea(l,b,h))
print("Cuboid Perimeter=",CubPerimeter(l,b,h))

