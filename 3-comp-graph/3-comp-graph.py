#-*-coding:utf8;-*-

'''
<!--@ Component of Graph @--!>

Comments:
In the 3-cgc-graph.in file, in first line, enter count of nodes. In the next
lines enter the links between the graph nodes in the form: node1 space node2.
Run the 3-cgc-graph.py file. In the file 3-cgc-graph.out, you will find the
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
    print(node_state)
    if node_state[2] == False: # it's line have error
        count += 1
        node_state = dfs(graph, node_state.index(False), node_state)
        comp(graph, node_state, count)
    return count


# Basic processes
graph = [[] for _ in range(count_of_nodes)]
for node in nodes: add_dep(node)

node_state = [False for _ in range(count_of_nodes)]
result = comp(graph, node_state, 1)


# Output values
file = open('3-comp-graph.out', 'w')
file.write(str(result) + '\n')
file.close()