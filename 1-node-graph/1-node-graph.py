#-*-coding:utf8;-*-


'''
<!--@ Find number of nodes and edges in graph @--!>

Comments:
In the 1-node-graph.in file, type "n" and the number of nodes in the graph, if
you want to find the number of edges. Otherwise, enter "e" and the number of
edges if you want to find the number of nodes. Run the 1-node-graph.py file. In
the file 1-node-graph.out you will find number 0, if the search number is not
possible, otherwise you will find the desired number.

Author: Nazar Ponochevnyi
'''


# Input values
file = open('1-node-graph.in', 'r')
data = [d.strip() for d in file.readlines()]
file.close()


# Basic processes
result = 0
q = data[0]
inP = int(data[1])
if q == 'n' and ((inP * (inP - 1)) / 2) % 1 == 0:
    result = int((inP * (inP - 1)) / 2)
else:
    if q == 'e' and ((1 + (8 * inP)) ** 0.5) % 1 == 0:
        result = int((1 + (1 + (8 * inP)) ** 0.5) / 2)


# Output values
file = open('1-node-graph.out', 'w')
file.write(str(result) + '\n')
file.close()