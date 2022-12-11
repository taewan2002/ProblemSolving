import math

class Vertex :
    def __init__(self, name):
        self.name=name
        self.d=math.inf
        self.p=None

    def __str__(self):
        return self.name

class Edge:
    def __init__(self, src, dest, w):
        self.src=src
        self.dest=dest
        self.w=w

class Graph:
    def __init__(self, V, E):
        self.V=V
        self.E=E

    def __str__(self):
        s=''
        for e in self.E:
            s += e.src.name + '->' + e.dest.name + ', w = '+str(e.w) + '.\n'
        return s

    def shortest_path(self, nodeA, nodeB):
        self.belman_ford(nodeA)
        list=self.print_path(nodeA, nodeB, [])
        print('Shortest path:')
        for v in list:
            print (v)
        print('Duzina: ', nodeB.d)
        return None

    def print_path(self, u, v, list):
        if v is u:
            list.append(u)
        elif v.p is None:
            print('No path from', u, 'to', v)
            return None, None
        else:
            list=self.print_path(u, v.p, list)
            list.append(v)
        return list


    def belman_ford(self, s):
        self.init_single_source(s)
        for v in self.V:
            for e in self.E:
                self.relax(e.src, e.dest, self.get_weight(e.src, e.dest))
        for e in self.E:
            if e.dest.d > e.src.d + self.get_weight(e.src, e.dest):
                return False
        return True

    def get_weight(self, u, v):
        for e in self.E:
            if e.src == u  and e.dest == v:
                return e.w
        return math.inf

    def init_single_source(self, s):
        for v in self.V:
            v.d=math.inf
            v.p=None
        s.d=0

    def relax(self, u, v, w):
        if v.d>u.d+w:
            v.d=u.d+w
            v.p=u


u = Vertex('u')
v = Vertex('v')
x = Vertex('x')
w = Vertex('w')
y = Vertex('y')
z = Vertex('z')

V = [u, v, x, w, y, z]

# 경로와 cost
uv = Edge(u, v, 2)
ux = Edge(u, x, 1)
vx = Edge(v, x, 2)
vw = Edge(v, w, 3)
wy = Edge(w, y, 1)
xw = Edge(x, w, 3)
xy = Edge(x, y, 1)
yz = Edge(y, z, 2)
wz = Edge(w, z, 5)

E = [uv, ux, vx, vw, wy, xw, xy, yz, wz]

G = Graph(V, E)
print(G)

# 최단 경로
G.shortest_path(u, z)

