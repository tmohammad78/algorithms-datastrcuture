# Graph 

### BFS 
BFS is the graph use the queue and a array to store node that visited

### DFS
DFS use stack and replace older node with the nodes that can reach 

### Topology sort
The topological sort algorithm takes a directed graph and returns an array of the nodes where each node appears before all the nodes it points to.

**note** : Cycylic graph dont have valid topological ordering \
For start , we begin with node that has no incomming directed edge , it must of zero indegree  \
**note:We have indegree and outdegree for directed graph** \
when we start with first node , we delete it and write nodes that are connected (notice that if we have cycle we should check our rules that wrote in the top)


### Usages 
* Job-shop scheduling
* Shorted path 