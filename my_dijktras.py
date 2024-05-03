import heapq

def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    pq = [(0, source)]
    
    while pq:
        dist, node = heapq.heappop(pq)
        for neighbor, weight in graph[node]:
            alt = distances[node] + weight
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                heapq.heappush(pq, (alt, neighbor))
    
    return distances

graph = {'A': [('B', 2), ('C', 4)],
         'B': [('A', 2), ('C', 1), ('D', 7)],
         'C': [('A', 4), ('B', 1), ('D', 3)],
         'D': [('B', 7), ('C', 3)]}

source = 'A'
shortest_distances = dijkstra(graph, source)
print("Shortest distances from", source, "to all other vertices:")
for vertex, distance in shortest_distances.items():
    print(f"To {vertex}: {distance}")
