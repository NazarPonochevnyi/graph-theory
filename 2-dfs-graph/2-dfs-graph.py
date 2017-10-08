#-*-coding:utf8;-*-

'''
@Search in graph@

Comments:
In the 2-dfs-graph.in file, enter the links between the graph nodes in the
form: node1 space node2. In the last line enter the name of the nodes, the
connection between which you want to check, in the form: node1 space node2.
Run the 2-dfs-graph.py file. In the file 2-dfs-graph.out, you will find the
number 1 if the connection is possible, else you will find the number 0.

Author: Nazar Ponochevnyi
'''


# Input values
file = open('2-dfs-graph.in', 'r')
data = [d.strip() for d in file.readlines()]
file.close()
nodes = data[:-1]
node1 = int(data[-1].split()[0])
node2 = int(data[-1].split()[1])


# Functions
def add_dep(n):
    n1 = int(n.split()[0])
    n2 = int(n.split()[1])
    node_state[n1] = False
    node_state[n2] = False
    if isinstance(graph.get(n1), list): graph[n1].append(n2)
    else: graph[n1] = [n2]
    if isinstance(graph.get(n2), list): graph[n2].append(n1)
    else: graph[n2] = [n1]

def dfs(graph, node, visited):
    if not node_state.get(node):
        node_state[node] = True
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


# Basic processes
graph = {}
node_state = {}
for node in nodes: add_dep(node)

visited = dfs(graph, node1, [])
result = 1 if node2 in visited else 0


# Output values
file = open('2-dfs-graph.out', 'w')
file.write(str(result) + '\n')
file.close()
