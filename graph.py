from Vertex import Vertex
from math import sqrt
from mathfns import *

class Graph:
    def __init__(self):
        self.vertices = {}
        self.graph = {}

    def add_vertex(self, x, y, name):
        vertex = Vertex(x, y, name)
        for vn in self.vertices:
            v = self.vertices[vn]
            if v.x == x and v.y == y:
                return v
        while vertex.name in self.vertices:
            vertex.name += "_copy"
        self.vertices[vertex.name] = vertex
        self.graph[vertex] = []
        return vertex

    def add_edge(self, v1, v2):
        if v1 in self.vertices.values() and v2 in self.vertices.values():
            if v1 == v2:
                pass
            else:
                self.graph[v1].append(v2)
                self.graph[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 in self.vertices.values() and v2 in self.vertices.values():
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)

    def add_intersection_vertex(self, s1, e1, s2, e2):
        int_x, int_y = find_line_intersection(s1.x, s1.y, e1.x, e1.y, s2.x, s2.y, e2.x, e2.y)
        if int_x is not None and int_y is not None and e1 in self.graph[s1] and e2 in self.graph[s2]:
            int_name = "Intersection_" + str(s1.name) + "-" + str(e1.name) + "," + str(s2.name) + "-" + str(e2.name)
            intersection = self.add_vertex(int_x, int_y, int_name)
            self.remove_edge(s1, e1)
            self.remove_edge(s2, e2)
            for x in [s1, s2, e1, e2]:
                self.add_edge(x, intersection)
            return intersection
        return False

    def add_midpoint(self, s, e, m):
        if is_on_line(s.x, s.y, e.x, e.y, m.x, m.y) and e in self.graph[s] and s in self.graph[e] and m in self.graph:
            self.remove_edge(s, e)
            self.remove_edge(e, s)
            for x in [s, e]:
                self.add_edge(x, m)
            return True
        else:
            return False

    def gen_vertex_id_dict(self):
        vertex_ids = {}
        id_vertices = {}
        for ind, x in enumerate(self.graph):
            vertex_ids[x] = ind
            id_vertices[ind] = x
        return vertex_ids, id_vertices

    def generate_matrix(self):
        graph = [[float('Inf') for x in range(len(self.vertices))] for y in range(len(self.vertices))]
        vertex_ids, _ = self.gen_vertex_id_dict()
        for s in self.graph:
            for e in self.graph[s]:
                i = vertex_ids[s]
                j = vertex_ids[e]
                d = sqrt((s.x - e.x) ** 2 + (s.y - e.y) ** 2)
                graph[i][j] = d
        return graph

    def fw(self):
        graph = self.generate_matrix()

        V = len(graph)
        d = list(map(lambda i: list(map(lambda j: j, i)), graph))
        n = [[None for x in range(V)] for y in range(V)]
        for i in range(V):
            for j in range(V):
                if d[i][j] != float('Inf'):
                    n[i][j] = j

        for i in range(V):
            d[i][i] = 0
            n[i][i] = i

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]
                        n[i][j] = n[i][k]
        return d, n

    def path(self, sv, ev):
        vdict, iddict = self.gen_vertex_id_dict()

        s = vdict[sv]
        e = vdict[ev]
        d, n = self.fw()
        ds = d[s][e]
        if not n[s][e]:
            return [], float('Inf')
        else:
            path = [sv]
            while s != e:
                s = n[s][e]
                path.append(iddict[s])
            return path, ds

    def add_endpoint(self, v):
        min_dist = float('Inf')
        min_s = None
        min_e = None
        m = None
        for i in self.graph:
            for j in self.graph[i]:
                ptx, pty = pt_line(i.x, i.y, j.x, j.y, v.x, v.y)
                d = distance(ptx, pty, v.x, v.y)
                if d < min_dist or (d == min_dist and 0 < distance(i.x, i.y, j.x, j.y) < distance(min_s.x, min_s.y, min_e.x, min_e.y)):
                    min_dist = d
                    min_s = i
                    min_e = j
                    mx, my = (ptx, pty)
        m = self.add_vertex(mx, my, "connection")
        print(min_s, min_e, m, m == min_s, m == min_e)
        print(is_on_line(min_s.x, min_s.y, min_e.x, min_e.y, m.x, m.y))
        self.add_midpoint(min_s, min_e, m)
        self.add_edge(v, m)

    def __str__(self):
        s = ""
        for x in self.graph:
            s += str(x) + " @ (" + str(x.x) + ", " +  str(x.y) + ") : " + str([str(y) for y in self.graph[x]]) + "\n"
        return s





