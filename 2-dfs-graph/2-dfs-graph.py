#-*-coding:utf8;-*-

'''
<!--@ Search in graph @--!>

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
    if isinstance(graph.get(n1), list): graph[n1].append(n2)
    else: graph[n1] = [n2]
    if isinstance(graph.get(n2), list): graph[n2].append(n1)
    else: graph[n2] = [n1]

def dfs(graph, node, node_state):
    if not node_state[node - 1]:
        node_state[node - 1] = True
        for n in graph[node]:
            dfs(graph, n, node_state)
    return node_state


# Basic processes
graph = {}
for node in nodes: add_dep(node)

node_state = dfs(graph, node1, [False for _ in range(len(graph.keys()))])
result = 1 if node_state[node2] else 0


# Output values
file = open('2-dfs-graph.out', 'w')
file.write(str(result) + '\n')
file.close()
