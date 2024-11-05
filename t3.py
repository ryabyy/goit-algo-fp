import heapq

def dijkstra(graph, start):
	queue = []
	heapq.heappush(queue, (0, start))
	visited = set()

	shortest_paths = {vertex: float('infinity') for vertex in graph}
	shortest_paths[start] = 0

	while queue:
		current_distance, current_vertex = heapq.heappop(queue)
		if current_vertex in visited:
			continue
		
		visited.add(current_vertex)
		
		for neighbor, weight in graph[current_vertex].items():
			distance = current_distance + weight
			if distance < shortest_paths[neighbor]:
				shortest_paths[neighbor] = distance
				heapq.heappush(queue, (distance, neighbor))
	return shortest_paths

graph = {
	'A': {'B': 1, 'C': 4},
	'B': {'A': 1, 'C': 2, 'D': 5},
	'C': {'A': 4, 'B': 2, 'D': 1},
	'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)
print(shortest_paths)