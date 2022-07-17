import numpy as np
from math import sqrt
def find_line_intersection(x1,y1,x2,y2,x3,y3,x4,y4):
    mat = np.matrix([[x2 - x1, x3 - x4], [y2 - y1, y3 - y4]])
    vec = np.array([[x3 - x1], [y3 - y1]])
    a, b = -1, -1
    if np.linalg.det(mat) != 0:
        s = np.linalg.solve(mat, vec)
        a, b = float(s[0]), float(s[1])
    if 0 < a < 1 and 0 < b < 1:
        int_x = x1 + (x2 - x1) * a
        int_y = y1 + (y2 - y1) * a
        return int_x, int_y
    return None, None

def is_on_line(x1,y1,x2,y2,ptx,pty):
    x1 = round(x1, 3)
    y1 = round(y1, 3)
    x2 = round(x2, 3)
    y2 = round(y2, 3)
    ptx = round(ptx, 3)
    pty = round(pty, 3)
    if y1 == y2:
        if (x1 < ptx < x2 or x2 < ptx < x1) and pty == y1:
            return True
        else:
            return False
    elif x1 == x2:
        if (y1 < pty < y2 or y2 < pty < y1) and ptx == x1:
            return True
        else:
            return False
    else:
        tx = (ptx - x1) / (x2 - x1)
        ty = (pty - y1) / (y2 - y1)
        if round(tx, 3) == round(ty, 3) and 0 < tx < 1:
            return True
        else:
            return False

def distance(x1,y1,x2,y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# distance from a point to a line segment:
def pt_line(x1,y1,x2,y2,ptx,pty):
    if is_on_line(x1,y1,x2,y2,ptx,pty):
        return (ptx, pty)
    dotprod = (x2 - x1) * (ptx - x1) + (y2 - y1) * (pty - y1)
    try:
        param = dotprod / (distance(x1, y1, x2, y2) ** 2)
    except ZeroDivisionError:
        return (ptx, pty)
    if 0 <= param <= 1:
        return (x1 + param * (x2 - x1), y1 + param * (y2 - y1))
    elif param < 0:
        return (x1, y1)
    else:
        return (x2, y2)

#scale:
def xy_to_pix(W, H, SF, x, y):
    X = (x / SF + W)
    Y = (H - y / SF)
    return X, Y

def circle_coords(x, y, r):
    return x - r, y - r, x + r, y + r
