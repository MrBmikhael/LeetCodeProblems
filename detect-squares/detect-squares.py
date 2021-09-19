# https://www.youtube.com/watch?v=bahebearrDc

class DetectSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)
        self.points = []
        
    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point
        
        for x, y in self.points:
            if (abs(py-y) != abs(px-x)) or x == px or y == py:
                continue
            count += self.pointCount[(x,py)] * self.pointCount[(px, y)]
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)