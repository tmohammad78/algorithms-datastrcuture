import graph as g 

def sortUnit(myGraph,currentNode,visited,result):
    visited[currentNode] = True
    for i in myGraph.graph[currentNode]:
        if visited[i] == False:
            sortUnit(myGraph,i,visited,result)
    result.insert(0,currentNode)

def topologicalSort(graph):
    visited = [False] * graph.vertices
    result = []
    for currenctNode in range(graph.vertices):
        if visited[currenctNode] == False:
            sortUnit(myGraph , currenctNode , visited , result)
    return result
myGraph = g.Graph(5)

myGraph.addEdge(0, 1) 
myGraph.addEdge(0, 3) 
myGraph.addEdge(1, 2) 
myGraph.addEdge(2, 3) 
myGraph.addEdge(2, 4) 
myGraph.addEdge(3, 4) 

print(topologicalSort(myGraph))
