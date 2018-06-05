import math

# ===============  Point Class 定义 =================
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return "Point({0.x!r},{0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r},{0.y!r})".format(self)

a = Point()

print("repr(a)=" + repr(a))
b = Point(3,4)
print("str(b)=" + str(b))
b.distance_from_origin()
b.x = -19
print("str(b)=" + str(b))
print(a==b,a!=b)

# 利用eval，把表达式转化为Point类
p = Point(3,9)
print("repr(p)=" + repr(p))
q = eval(repr(p))
print(type(q))
print(repr(q))

# ===============  Circle Class 定义 =================
class Circle(Point):
    def __init__(self, radius, x=0,y=0):
        super().__init__(x,y)
        self.radius = radius

    @property    
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius )
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2 )
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def __eq__(self, other):
        return self.radius == other.radius and super.__eq__(other)
    
    def __repr__(self):
        return "Circle({0.radius!r},{0.x!r},{0.y!r})".format(self)
    
    def __str__(self):
        return repr(self)


c = Circle(5,6,7)

print(c.area)
print(c.edge_distance_from_origin)

