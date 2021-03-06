import sys
import math

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

nodes = []
for i in range(n):
    nodes.append(i)

print(f"nodes {nodes}", file=sys.stderr)

links = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links.append([n1, n2])

print(f"links {links}", file=sys.stderr)

gateways = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)

print(f"gateways {gateways}", file=sys.stderr)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


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

def sort_dict(my_dict, mode=0):
    '''if mode = 0 then sorts by value'''
    if mode==0:
        sorted_dict = {
            k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])
        }
    elif mode==1:
        sorted_dict = {
            k: v for k, v in sorted(my_dict.items(), key=lambda item: item[0])
        }
    return sorted_dict

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



def build_critical_links():

    critical_links = []
    for g in gateways:
        for n in links:
            if n[0] == int(g) or n[1] == int(g):
                critical_links.append(n)
    print(f"critical links {critical_links}", file=sys.stderr)
    return critical_links


def make_nodes_next_to_gates_dict():
    nodes_next_to_gates = []
    for c in critical_links:
        if c[0] not in gateways and c[0] not in nodes_next_to_gates:
            nodes_next_to_gates.append(c[0])
        if c[1] not in gateways and c[1] not in nodes_next_to_gates:
            nodes_next_to_gates.append(c[1])

    nodes_next_to_gates_dict = {i: 0 for i in nodes_next_to_gates}

    for c in critical_links:
        for n in c:
            if n in nodes_next_to_gates_dict:
                nodes_next_to_gates_dict[n] += 1

    print(f"nodes next to gates dict {nodes_next_to_gates_dict}", file=sys.stderr)

    return nodes_next_to_gates_dict


def find_link_to_cut(gateway, node):
    print(f"finding link to cut", file=sys.stderr)
    for l in links:
        print(f"link {l}", file=sys.stderr)
        if l[0] == gateway and l[1] == node:
            link_to_cut = [l[0], l[1]]
            return link_to_cut
        elif l[0] == node and l[1] == gateway:
            link_to_cut = [l[0], l[1]]
            return link_to_cut
        
    return 0 # if can't find it


critical_links = build_critical_links()
nodes_next_to_gates_dict = make_nodes_next_to_gates_dict()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    print(f"si {si}", file=sys.stderr)

    critical_links = build_critical_links()
    nodes_next_to_gates_dict = make_nodes_next_to_gates_dict()

    link_to_cut = ''

    gateway_dict = {i: 999 for i in gateways}
    for g in gateways:
        gateway_dict[g] = dijkstra(g, si, nodes, links)

    print(f"gateway_dict {gateway_dict}", file=sys.stderr)

    most_important_node = max(nodes_next_to_gates_dict, key=nodes_next_to_gates_dict.get)
    most_important_gateway = min(gateway_dict, key=gateway_dict.get)
    print(f"most_important_node {most_important_node}", file=sys.stderr)
    print(f"most_important_gateway {most_important_gateway}", file=sys.stderr)

    link_to_cut = find_link_to_cut(most_important_gateway, most_important_node)

    print(f"link_to_cut {link_to_cut}", file=sys.stderr)

    links.remove(link_to_cut)
    
    # Example: 0 1 are the indices of the links you wish to sever the link between
    print(f"{link_to_cut[0]} {link_to_cut[1]}")
