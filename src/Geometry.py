class Point():
    def __init__(self, x, y) -> None:
        self.x = float(x)
        self.y = float(y)
    
    def __str__(self):
        pass
        # return f"({self.x}, {self.y})"

    def __eq__(self, other):
        pass
        # return True if ((self.x == other.x) and (self.y == other.y)) else False

    def __ne__(self, other):
        pass
        # return True if ((self.x != other.x) or (self.y != other.y)) else False

class Flate():
    def __init__(self, n) -> None:
        self.flate = [[False for _ in range(n)] for _ in range(n)]
    
    def place_point(self, point:Point):
        self.flate[point.x][point.y] = True
    
    def print_flate(self):
        for i in range(len(self.flate)):
            print(self.flate[i])
    