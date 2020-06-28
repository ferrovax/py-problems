# 16.3

def intersection(start1, end1, start2, end2):
    # orient the segments
    if start1.x > end1.x:
        swap(start1, end1)

    if start2.x > end2.x:
        swap(start2, end2)

    if start1.x > start2.x:
        swap(start1, start2)
        swap(end1, end2)

    line1 = Line(start1, end1)
    line2 = Line(start2, end2)

    # handle parallel cases
    if line1.slope == line2.slope:
        if line1.intercept == line2.intercept and isBetween(start1, start2, end1):
            return start2

        return None

    x = (line2.intercept - line1.intercept) / (line1.slope - line2.slope)
    y = line1.slope * x + line1.intercept

    intersection = Point(x, y)

    if isBetween(start1, intersection, end1) and isBetween(start2, intersection, end2):
        return intersection

    return None

# ------------------------------------------------------------------------------

def swap(ptA, ptB):
    x, y = ptA.x, ptA.y

    ptA.setLocation(ptB.x, ptB.y)
    ptB.setLocation(x, y)

def isBetween(start, mid, end):
    return between(start.x, mid.x, end.x) and between(start.y, mid.y, end.y)

def between(start, mid, end):
    return (end <= mid and mid <= start) if start > end else (start <= mid and mid <= end)

# ------------------------------------------------------------------------------

class Line:
    def __init__(self, start, end):
        self.slope = (end.y - start.y) / (end.x - start.x)
        self.intercept = end.y - self.slope * end.x

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def setLocation(self, x, y):
        self.x, self.y = x, y
