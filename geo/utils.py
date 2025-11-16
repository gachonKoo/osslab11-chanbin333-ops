import math

def distance(x1, y1, x2, y2):
    """두 점 (x1, y1), (x2, y2)의 거리 계산"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def area_of_triangle(base, height):
    """삼각형의 넓이 계산"""
    return 0.5 * base * height

