#-*-coding:utf8;-*-

'''
<!--@ Component of Graph @--!>

Comments:
In the 3-comp-graph.in file, in first line, enter count of nodes. In the next
lines enter the links between the graph nodes in the form: node1 space node2.
Run the 3-comp-graph.py file. In the file 3-comp-graph.out, you will find the
component of the graph.

Author: Nazar Ponochevnyi
'''


# Input values
file = open('3-comp-graph.in', 'r')
data = [d.strip() for d in file.readlines()]
file.close()
count_of_nodes = int(data[0])
nodes = data[1:]


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

def comp(graph, node_state, count):
    if False in node_state:
        node_state = dfs(graph, node_state.index(False), node_state)
        return comp(graph, node_state, count + 1)
    return count


# Basic processes
graph = []
node_state = []
for _ in range(count_of_nodes):
    graph.append([])
    node_state.append(False)
for node in nodes: add_dep(node)
result = comp(graph, node_state, 0)


# Output values
file = open('3-comp-graph.out', 'w')
file.write(str(result) + '\n')
file.close()
