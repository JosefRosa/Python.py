import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    visited = set()
    result = []

    while len(visited) < len(graph):
        current_node = None
        for node in graph:
            if node not in visited and (current_node is None or distances[node] < distances[current_node]):
                current_node = node

        visited.add(current_node)
        current_distance = distances[current_node]
        
        result.append({'node': current_node, 'distance': current_distance})

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return result

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node = 'A'
result = dijkstra(graph, start_node)
print(result)
