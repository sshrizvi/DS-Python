class Point2D:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        point = '<{},{}>'.format(self.x, self.y)
        return point
    
    def euclidean_distance(self, other) -> float:
        d = ((other.x - self.x)**2 + (other.y - self.y)**2) ** (1/2)
        return d
    
    def distance_from_origin(self) -> float:
        d = ((0 - self.x)**2 + (0 - self.y)**2) ** (1/2)
        return d
    
    def point_on_line(self, line) -> bool:
        if((line.a*self.x + line.b*self.y + line.c) == 0):
            return True
        else:
            return False
        
    def distance_from_point_to_line(self, line) -> float:
        d = abs(line.a*self.x + line.b*self.y + line.c) / ((line.a**2 + line.b**2)**(1/2))
        return d
    
class Line:

    def __init__(self, a:int, b:int, c:int) -> None:
        
        if(a != 0):
            self.a = a
        else:
            raise ValueError('Coeffiecient of x cannot be equal to Zero :(')
        if(b != 0):
            self.b = b
        else:
            raise ValueError('Coeffiecient of y cannot be equal to Zero :(')
        self.c = c

    def __str__(self) -> str:
        pass


# Driver Code
point1 = Point2D(1,1)
point2 = Point2D(1,2)
line = Line(1, 1, -2)
print(point1.distance_from_point_to_line(line))