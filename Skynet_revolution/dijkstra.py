nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
links = [[2, 6], [9, 7], [0, 7], [9, 8], [8, 2], [7, 1], [9, 2], [3, 1], [2, 5], [0, 8], [4, 1], [9, 1], [0, 9], [2, 1]]


def dijkstra(n1, n2, nodes, links):
    '''Get shortest distance between two nodes

    Assumes unweighted linkes (i.e. each link's value is 1)
    '''
    node_dict = {i: 999 for i in nodes}

    node_dict[n1] = 0
    checked = []

    traverse_tree(n1, node_dict, links, checked)

    distance = node_dict[n2]

    return distance


def traverse_tree(node, node_dict, links, checked):

    print(node_dict)

    distance = node_dict[node] + 1

    adjacent_nodes = get_adjacent_nodes(node, links)

    for an in adjacent_nodes:
        if node_dict[an] > distance:
            node_dict[an] = distance

    checked.append(node)

    current_node = set_current_node(checked, node_dict)

    if current_node == 0:
        return 0

    traverse_tree(current_node, node_dict, links, checked)


def get_adjacent_nodes(node, links):
    adjacent_nodes = []
    for l in links:
        if l[0] == node:
            if l[1] not in adjacent_nodes:
                adjacent_nodes.append(l[1])
        if l[1] == node:
            if l[0] not in adjacent_nodes:
                adjacent_nodes.append(l[0])
    return adjacent_nodes


def set_current_node(checked, node_dict):
    # visited is a set that contains the names of the nodes
    # marked as visited. E.g. [1, 2].
    # currentDistances is a dictionary that contains the
    # current minimum distance of each node. E.g. {1: 0, 2: 1, 3: 2}

    sorted_dict = {
        k: v for k, v in sorted(node_dict.items(), key=lambda item: item[1])
    }

    for k in sorted_dict.keys():
        if k not in checked:
            return k
    return 0

print(dijkstra(1, 2, nodes, links))
