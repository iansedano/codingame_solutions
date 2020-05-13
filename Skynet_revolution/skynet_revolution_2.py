import sys
import math

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

critical_links=[]
for g in gateways:
    for n in links:
        if n[0] == int(g) or n[1] == int(g):
            critical_links.append(n)

print(f"critical links {critical_links}", file=sys.stderr)

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    print(f"si {si}", file=sys.stderr)

    node_to_cut = ''

    for cn in critical_nodes:
        if links[cn][1] == si or links[cn][2] == si:
            node_to_cut = links[cn]
            critical_nodes.remove(cn)


    for cn in critical_nodes:
        if node_to_cut == '':
            node_to_cut = links[critical_nodes[0]]
            critical_nodes.pop(0)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # Example: 0 1 are the indices of the links you wish to sever the link between
    print(f"{node_to_cut[1]} {node_to_cut[2]}")
