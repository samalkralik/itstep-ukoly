# funkce.py
data = []


def moje_funkce(a, b):
    c = a + b
    return c


vysl1 = moje_funkce(10, 20)
vysl2 = moje_funkce(110, 2)
vysl3 = moje_funkce(150, 220)
# print(vysl1)
# print(vysl2)
# print(vysl3)


def obvod_trojuhelnika(a, b, c):
    obvod = a + b + c
    return obvod


obvod1 = obvod_trojuhelnika(5, 52, 1)
print(obvod1)


def is_valid_triangle(a, b, c) -> bool:
    if (a + b) <= c:
        return False
    elif (a + c) <= b:
        return False
    elif (c + b) <= a:
        return False
    else:
        return True


def is_valid_triangle2(a, b, c):
    return (a + b) > c and (a + c) > b and (c + b) > a


import math


def obvod_kruhu(r):
    if r > 0:
        return 2 * r * math.pi
    else:
        return "invalid shape"


print(obvod_kruhu(5))
print(obvod_kruhu(0))


def obsah_kruhu(r):
    if r > 0:
        return math.pi * r**2
    else:
        return "invalid shape"


print(obsah_kruhu(10))
print(obsah_kruhu(0))


def get_quadrangle_type(a, b, c, d):
    # all angles are 90 degrees
    if a > 0 and b > 0 and c > 0 and d > 0:
        if a == b == c == d:
            return "square"
        elif (a == b and c == d) or (a == c and b == d):
            return "rectangular"
        else:
            return "irregular quadrilateral"
    else:
        return "invalid shape"


print(get_quadrangle_type(3, 2, 3, 2))
print(get_quadrangle_type(2, 2, 2, 2))
print(get_quadrangle_type(0, 2, 3, 3))
