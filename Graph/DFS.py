from collections import defaultdict

class DFS():

    def __init__(self,vertics):
        self.vertics = vertics
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def traversal(self,v):
        visited = [False for i in range(self.vertics)]
        stack =[]
        stack.append(v)
        while(len(stack)):
            last = stack[-1]
            stack.pop()
            if not (visited[last]):
                print(last,end = " ")
                visited[last] = True

            for node in self.graph[last]:
                if not visited[node]:
                    stack.append(node)

g  = DFS(5)
g.addEdge(1, 0);
g.addEdge(0, 2);
g.addEdge(2, 1);
g.addEdge(0, 3);
g.addEdge(1, 4);
 
print("Following is Depth First Traversal")
g.traversal(0)

