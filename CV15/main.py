class Node:
 
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.tmp_distance = 1_000_000
        self.visited = False
 
class Edge:
 
    def __init__(self, node_a, node_b, distance):
        self.node_a = node_a
        self.node_b = node_b
        self.distance = distance
 
def build_graph(file_path):
    file = open(file_path)
    content = file.readlines()
    nodes = {}
 
    # Vytvarime pouze uzly
    for line in content:
        items = line.split(",")
        node_a = items[0]
        node_b = items[1]
        if node_a not in nodes.keys():
            nodes[node_a] = Node(node_a)
           
        if node_b not in nodes.keys():
            nodes[node_b] = Node(node_b)
 
    #vytvarime hrany
    for line in content:
        items = line.split(",")
        node_a = items[0]
        node_b = items[1]
        distance = int(items[2])
        edge = Edge(nodes[node_a], nodes[node_b], distance)
        nodes[node_a].edges.append(edge)
        nodes[node_b].edges.append(edge)
 
    return list(nodes.values())

def find_shotest_edge(edges_list):
    min_value = edges_list[0].distance
    edge = edges_list[0]

    for e in edges_list:
        if min_value > e.distance:
            min_value = e.distance
            edge = e

    return edge

def prime(start_node):
    queue = [start_node]
    edges_list = []
    visited_nodes = [start_node]
    found_edge = []
    while len(queue) > 0:
        current_node = queue[0]
        edges_list.extend(current_node.edges) 
        edge = find_shotest_edge(edges_list)
        if edge.node_a in visited_nodes:
            new_node = edge.node_b
        else:
            new_node = edge.node_a

        if new_node in visited_nodes:
            edges_list.remove(edge)
            continue
        
        found_edge.append(edge)
        visited_nodes.append(new_node)
        if new_node not in visited_nodes:
            queue.append(new_node)

        del queue[0]
    
    return found_edge
 
if __name__ == "__main__":
    graph = build_graph("./CV15/graphs.csv")

    print(prime(graph[0]))
    