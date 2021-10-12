from pprint import pprint

class Graph:
    def __init__(self,vertices):
        self.vertices =vertices
        self.adj = [[] for i in range(vertices)]

    def addEdge(self,v,u,w):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])
        pprint(self.adj)

    def path(self,start, k):
        path =[False]*self.vertices
        path[start] = 1
        return self.pathCheck(start,k ,path)
    # This method should shortest path from start node
    def pathCheck(self,start,k,path):
        if k<= 0:
            return True
        i = 0 
        while i != len(self.adj[start]):
            weight = self.adj[start][i][1]
            vertices = self.adj[start][i][0]
            i +=1
            if path[vertices] == True:
                continue

            if (weight >= k):
                return True
            path[vertices]=True

            if (self.pathCheck(vertices, k-weight, path)):
                return True
       
            # Backtrack
            path[vertices] = False
        return False

g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

print(g.adj)

if g.path(0,62):
    print("yes")
else :
    print("no")

if g.path(0,59):
    print("yes")
else :
    print("no")