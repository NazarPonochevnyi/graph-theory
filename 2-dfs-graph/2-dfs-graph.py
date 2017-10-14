#-*-coding:utf8;-*-

'''
<!--@ Search in graph @--!>

Comments:
In the 2-dfs-graph.in file, in first line, enter count of nodes, in the next
line, enter the name of the nodes, the connection between which you want to
check, in the form: node1 space node2. In the next lines enter the links
between the graph nodes in the form: node1 space node2. Run the 2-dfs-graph.py
file. In the file 2-dfs-graph.out, you will find the number 1 if the connection
is possible, else you will find the number 0.

Author: Nazar Ponochevnyi
'''


# Input values
file = open('2-dfs-graph.in', 'r')
data = [d.strip() for d in file.readlines()]
file.close()
count_of_nodes = int(data[0])
node1 = int(data[1].split()[0]) - 1
node2 = int(data[1].split()[1]) - 1
nodes = data[2:]


# Functions
def add_dep(n):
    n1 = int(n.split()[0]) - 1
    n2 = int(n.split()[1]) - 1
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(graph, node, node_state):
    if not node_state[node]:
        node_state[node] = True
        for n in graph[node]:
            dfs(graph, n, node_state)
    return node_state


# Basic processes
graph = [[] for _ in range(count_of_nodes)]
for node in nodes: add_dep(node)

node_state = dfs(graph, node1, [False for _ in range(count_of_nodes)])
result = 1 if node_state[node2] else 0


# Output values
file = open('2-dfs-graph.out', 'w')
file.write(str(result) + '\n')
file.close()
