class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        for i in range(len(rectangles)):
            w, h = rectangles[i]
            ratio = w / h
            if ratio not in ratios:
                ratios[ratio] = [rectangles[i]]
            else:
                ratios[ratio].append(rectangles[i])
        output = 0
        for i in ratios.keys():
            if len(ratios[i]) > 1:
                output += ((len(ratios[i])) * (len(ratios[i]) - 1)) / 2
        return int(output)
        