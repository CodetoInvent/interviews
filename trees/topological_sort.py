from tree import *

def topological_sort(graph):
    visited = set()
    stack = []
    
    for node in graph.nodes:
        if node in visited: continue
        traverse_node(node)


def traverse_node(root, visited, stack):
    visited.add(node)

    for child in node.adjacent:
        if child in visited: continue
        traverse_node(child)

    stack.append(node)

