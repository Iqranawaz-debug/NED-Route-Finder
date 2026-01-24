import openrouteservice

client = openrouteservice.Client(key='5b3ce3597851110001cf624858e70af3a23c4d788042edb881c991101') 

# Define the locations with their coordinates
locations = {
    'Millennium Mall': [67.1089, 24.9037],
    'Ayesha Manzil': [67.0615, 24.9322],
    'Korangi': [67.1411, 24.8356],
    'Shahrah-e-Faisal': [67.0733, 24.8706],
    'Gulshan Chowrangi': [67.0913, 24.9224],
    'NIPA': [67.0956, 24.9236],
    'NED University': [67.1110, 24.9314],
    'Malir Halt': [67.2060, 24.8940],
    'Safoora Chowrangi': [67.1290, 24.9260],
    'Nazimabad No. 7': [67.0300, 24.9200],
    'Sakhi Hassan': [67.0300, 24.9500],
    'Shah Faisal Colony': [67.1500, 24.8600],
    'Drigh Road': [67.1300, 24.8800]
}

# Define the route pairs
route_pairs = [
    ('Millennium Mall', 'NIPA'),
    ('Ayesha Manzil', 'Gulshan Chowrangi'),
    ('Gulshan Chowrangi', 'NIPA'),
    ('NIPA', 'NED University'),
    ('Korangi', 'Shahrah-e-Faisal'),
    ('Shahrah-e-Faisal', 'NIPA'),
    ('Malir Halt', 'Safoora Chowrangi'),
    ('Safoora Chowrangi', 'NED University'),
    ('Nazimabad No. 7', 'Sakhi Hassan'),
    ('Sakhi Hassan', 'NIPA'),
    ('Shah Faisal Colony', 'Drigh Road'),
    ('Drigh Road', 'NIPA')
]

# Function to get distance between two coordinates
def get_distance(from_coord, to_coord):
    route = client.directions(
        coordinates=[from_coord, to_coord],
        profile='driving-car',
        format='geojson'
    )
    return route['features'][0]['properties']['summary']['distance'] / 1000  # km

# Calculate distances for all route pairs
distances = {}
for start, end in route_pairs:
    dist = get_distance(locations[start], locations[end])
    distances[(start, end)] = round(dist, 2)

# Print the distances
print(distances)


# Step 1: Graph setup
distances = {
    ('Millennium Mall', 'NIPA'): 4.47,
    ('Ayesha Manzil', 'Gulshan Chowrangi'): 4.46,
    ('Gulshan Chowrangi', 'NIPA'): 1.31,
    ('NIPA', 'NED University'): 2.87,
    ('Korangi', 'Shahrah-e-Faisal'): 11.14,
    ('Shahrah-e-Faisal', 'NIPA'): 9.29,
    ('Malir Halt', 'Safoora Chowrangi'): 14.19,
    ('Safoora Chowrangi', 'NED University'): 3.61,
    ('Nazimabad No. 7', 'Sakhi Hassan'): 4.64,
    ('Sakhi Hassan', 'NIPA'): 10.9,
    ('Shah Faisal Colony', 'Drigh Road'): 9.07,
    ('Drigh Road', 'NIPA'): 12.87
}

graph = {}
for (start, end), distance in distances.items():
    if start not in graph:
        graph[start] = []
    graph[start].append((end, distance))

def dijkstra(graph, start):
    unvisited = set(graph.keys())
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0

    while unvisited:
        current = None
        min_distance = float('inf')
        for node in unvisited:
            if distances.get(node, float('inf')) < min_distance:
                current = node
                min_distance = distances[node]

        if current is None:
            break

        unvisited.remove(current)

        for neighbor, weight in graph.get(current, []):
            if distances[current] + weight < distances.get(neighbor, float('inf')):
                distances[neighbor] = distances[current] + weight
                previous[neighbor] = current

    return distances, previous

def get_path(previous, start, end):
    path = []
    current = end
    while current and current != start:
        path.append(current)
        current = previous.get(current)
    if current == start:
        path.append(start)
        path.reverse()
        return path
    return None

sources = ['Millennium Mall', 'Ayesha Manzil', 'Korangi', 'Malir Halt', 'Nazimabad No. 7', 'Shah Faisal Colony']
destination = 'NED University'

shortest_path = None
shortest_distance = float('inf')
best_source = None

for source in sources:
    all_distances, previous_nodes = dijkstra(graph, source)
    dist = all_distances.get(destination, float('inf'))
    if dist != float('inf'):
        path = get_path(previous_nodes, source, destination)
        print(f"{source} → NED University:")
        print(f"  Path: {' → '.join(path)}")
        print(f"  Distance: {round(dist, 2)} km\n")
        if dist < shortest_distance:
            shortest_path = path
            shortest_distance = dist
            best_source = source
    else:
        print(f"{source} → NED University: No path found\n")

print("📍 Shortest Path Overall:")
print(f"From {best_source}: {' → '.join(shortest_path)}")
print(f"Total Distance: {round(shortest_distance, 2)} km")

print(f"{'Source':<20}{'Path':<60}{'Distance (km)'}")
print("-" * 85)  
for source in sources:
    all_distances, previous_nodes = dijkstra(graph, source)
    dist = all_distances.get(destination, float('inf'))

    if dist != float('inf'):
        path = get_path(previous_nodes, source, destination)
        print(f"{source:<20}{' → '.join(path):<60}{round(dist, 2):<15}")
    else:
        print(f"{source:<20}{'No path found':<60}{'N/A':<15}")

graph = {
    'Millennium Mall': [('NIPA', 4.47), ('Ayesha Manzil', 5.0)],
    'Ayesha Manzil': [('Gulshan Chowrangi', 4.46)],
    'Korangi': [('Shahrah-e-Faisal', 11.14)],
    'NIPA': [('NED University', 2.87)],
    'Shahrah-e-Faisal': [('NIPA', 9.29)],
    'Gulshan Chowrangi': [('NIPA', 1.31)],
    'Malir Halt': [('Safoora Chowrangi', 14.19)],
    'Safoora Chowrangi': [('NED University', 3.61)],
    'Nazimabad No. 7': [('Sakhi Hassan', 4.64)],
    'Sakhi Hassan': [('NIPA', 10.9)],
    'Shah Faisal Colony': [('Drigh Road', 9.07)],
    'Drigh Road': [('NIPA', 12.87)],
    'NED University': [] 
}

def dijkstra(graph, start, end):
    unvisited = list(graph.keys())
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0

    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current)

        if current == end:
            break

        for neighbor, weight in graph[current]:
            new_distance = distances[current] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current

    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous_nodes[current]
    return distances[end], path

start = 'Millennium Mall'
end = 'NED University'
d_dist, d_path = dijkstra(graph, start, end)

print("Dijkstra's Algorithm:")
print(f"Path: {d_path}")
print(f"Total Distance: {d_dist:.2f} km")
print(f"Estimated Time: {d_dist / 40 * 60:.1f} min")

def simple_distance(coord1, coord2):
    x = (coord2[0] - coord1[0]) * 111
    y = (coord2[1] - coord1[1]) * 111
    return (x**2 + y**2) ** 0.5

def a_star(graph, start, end, coordinates):
    open_list = [start]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = simple_distance(coordinates[start], coordinates[end])

    while open_list:
        current = min(open_list, key=lambda node: f_score[node])
        if current == end:
            break
        open_list.remove(current)

        for neighbor, weight in graph[current]:
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + simple_distance(coordinates[neighbor], coordinates[end])
                if neighbor not in open_list:
                    open_list.append(neighbor)

    path = []
    current = end
    while current in came_from:
        path.insert(0, current)
        current = came_from[current]
    if path:
        path.insert(0, start)
    return g_score[end], path

coordinates = {
    'Millennium Mall': (24.9037, 67.1089),
    'Ayesha Manzil': (24.9322, 67.0615),
    'Korangi': (24.8356, 67.1411),
    'NIPA': (24.9236, 67.0956),
    'Shahrah-e-Faisal': (24.8706, 67.0733),
    'Gulshan Chowrangi': (24.9224, 67.0913),
    'Malir Halt': (24.8923, 67.1156),
    'Safoora Chowrangi': (24.8703, 67.0634),
    'Nazimabad No. 7': (24.9385, 67.0625),
    'Sakhi Hassan': (24.9210, 67.0593),
    'Shah Faisal Colony': (24.8614, 67.1346),
    'Drigh Road': (24.8771, 67.0514),
    'NED University': (24.9314, 67.1110)
}

print("\n A* Algorithm \n")
print("\n📍 Available Locations:")
for idx, loc in enumerate(coordinates):
    print(f"{idx + 1}. {loc}")

try:
    choice = int(input("\nEnter the number corresponding to your source location: "))
    source = list(coordinates.keys())[choice - 1]

    distance, path = a_star(graph, source, destination, coordinates)
    if distance == float('inf') or not path:
        print(f"\n🚫 No path found from {source} to {destination}.")
    else:
        print(f"\n✅ Shortest Path from {source} to {destination}:")
        print(f"  Path: {' → '.join(path)}")
        print(f"  Total Distance: {round(distance, 2)} km")

except (IndexError, ValueError):
    print("\n⚠️ Invalid selection. Please enter a valid number from the list.")
