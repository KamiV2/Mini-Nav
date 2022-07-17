import tkinter as tk
class Vertex:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self.name)