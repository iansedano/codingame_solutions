'''
Adjacency matrix.

BCN ------- LON
|
|
|
GLA

    BCN LON GLA
BCN  0   1   1
LON  1   0   0
GLA  1   0   0


Path

a sequence of edges which connect a sequence of distinc vertices.

Dijkstras algorithm

Start at a node, mark distance 0.
For every other node at the moment mark distance infinity.
Check neighbours and find value of distance.
Replace infinity with distance.
Add origin to "checked list"
move to next node closest to origin.
Repeat process, and replace distance value of nodes if less
that what they already have.

Mark your selected initial node with a current distance of 0
and the rest with infinity.
Set the non-visited node with the smallest current distance
as the current node C.
For each neighbour N of your current node C:
add the current distance of C with the weight of the edge
connecting C-N.
If it's smaller than the current distance of N, set it as
the new current distance of N.
Mark the current node C as visited.
If there are non-visited nodes, go to step 2.
'''


def set_current_node(visited, currentDistances):
    # visited is a set that contains the names of the nodes
    # marked as visited. E.g. {'A', 'C'}.
    # currentDistances is a dictionary that contains the
    # current minimum distance of each node. E.g. {'A': 0, 'B': 3, 'C': 5}

    print(visited)
    print(currentDistances)

    sorted_dict = {
        k: v for k, v in sorted(currentDistances.items(), key=lambda item: item[1])
    }

    for k in sorted_dict.keys():
        if k not in visited:
            return k
