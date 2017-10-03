#-*-coding:utf8;-*-
#qpy:3
#qpy:console

'''
@Search in graph@

Comments:
In the graph.in file, enter the links between the graph nodes in the form: 
node1 space node2. In the last line enter the name of the nodes, the connection
between which you want to check, in the form: node1 space node2. Run the 
graph.py file. In the file graph.out, you will find the number 1 if the 
connection is possible, else you will find the number 0.

Author: Nazar Ponochevnyi
'''


# Input values
file = open('2-dfs-graph.in', 'r')
data = [d.strip() for d in file.readlines()]
file.close()
nodes = data[:-1]
node1 = str(data[-1].split()[0])
node2 = str(data[-1].split()[1])


# Functions
def addDep(n):
    try:
        graph[n.split()[0]].append(n.split()[1])
    except:
        graph[n.split()[0]] = []
        graph[n.split()[0]].append(n.split()[1])
    try:
        graph[n.split()[1]].append(n.split()[0])
    except:
        graph[n.split()[1]] = []
        graph[n.split()[1]].append(n.split()[0])

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


# Basic processes
graph = {}
for node in nodes: addDep(node)

visited = dfs(graph, node1, [])
result = 0
if node2 in visited: result = 1


# Output values
file = open('2-dfs-graph.out', 'w')
file.write(str(result) + '\n')
file.close()
