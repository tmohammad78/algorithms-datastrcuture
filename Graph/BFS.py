from collections import defaultdict

class BFS():

    def __init__(self):
        self.graph = defaultdict(list)
        self.queue = []

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def traversal(self,s):
        visited = [False] * (max(self.graph) + 1)
        self.queue.append(s)
        visited[s] = True
        while self.queue:
            s = self.queue.pop(0)
            print(s,end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    self.queue.append(i)
                    visited[i] = True



graph  = BFS()
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,0)
graph.addEdge(1,3)
graph.addEdge(1,4)
graph.addEdge(2,0)
graph.addEdge(2,3)
graph.addEdge(3,1)
graph.addEdge(3,2)
graph.addEdge(3,4)
graph.addEdge(4,1)
graph.addEdge(4,3)

graph.traversal(2)

