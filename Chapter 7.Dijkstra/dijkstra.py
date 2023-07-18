graph = {}
graph["Book"] = {
    "Plastinka": 5,
    "Poster": 0
}
graph["Plastinka"] = {
    "Gitara": 15,
    "Drum": 20
}
graph["Poster"] = {
    "Gitara": 30,
    "Drum": 35
}
graph["Drum"] = {
    "Piano": 10
}
graph["Gitara"] = {
    "Piano": 20
}

graph["Piano"] = {}

costs = {
    "Plastinka": 5,
    "Poster": 0,
    "Drum": float('inf'),
    "Gitara": float('inf'),
    "Piano": float('inf')
}
processed = []

parents = {
    "Plastinka": "Book",
    "Poster": "Book"
}


def find_lowest_cost_node(costs: dict):
    lowest_cost = float('inf')
    lowest_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_node = node
    return lowest_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for neighbour in neighbours.keys():
        new_cost = cost + neighbours[neighbour]
        if costs[neighbour] > new_cost:
            costs[neighbour] = new_cost
            parents[neighbour] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
current_node = 'Piano'
final_way = ''
while current_node != 'Book':
    final_way = final_way + current_node + '<---'
    current_node = parents[current_node]

print(final_way[:-4:] + '<---' + 'Book')
