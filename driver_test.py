from graph import Graph
import tkinter as tk
from mathfns import *
from time import sleep
import pyautogui

m = Graph()


a = m.add_vertex(30, 300, "a")
b = m.add_vertex(40, 122, "b")
c = m.add_vertex(300, 40, "c")
d = m.add_vertex(111, 300, "d")
e = m.add_vertex(750, 430, "e")
f = m.add_vertex(600, 290, "f")

g = m.add_vertex(700, 100, "START")
h = m.add_vertex(124,450, "END")

m.add_edge(a, b)
m.add_edge(c, d)
m.add_edge(a, e)
m.add_edge(b, f)
m.add_edge(f, c)
i = m.add_intersection_vertex(f, b, c, d)
try:
    m.add_midpoint(b, i, e)
except:
    pass
#
m.add_endpoint(g)
m.add_endpoint(h)
#
p = m.path(g, h)[0]

win = tk.Tk()
win.geometry("800x800")
c = tk.Canvas(win, width=800, height=800)
ppairs = []
for i in range(len(p)):
    if i == 0:
        pass
    else:
        ppairs.append([p[i-1], p[i]])
c.pack()
print(m)
img = tk.PhotoImage(file="mappic.png")
c.create_image(400, 400, image=img)
for vn in m.vertices:
    v = m.vertices[vn]
    cx, cy = v.x, v.y
    xi, yi, xf, yf = circle_coords(cx, cy, 5)
    c.create_oval(xi,yi,xf,yf)
    c.create_text(cx+15,cy-10,text=vn)
for vs in m.graph:
    for ve in m.graph[vs]:
        sx, sy = vs.x, vs.y
        ex, ey = ve.x, ve.y
        if [vs, ve] in ppairs:
            w = 5
        else:
            w = 1
        c.create_line(sx, sy, ex, ey, width=w)



