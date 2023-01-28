# Ant Colony Optimization implementation for Travelling Salesman Problem

import random

# Number of cities
num_cities = 5

# Distance matrix
distances = [[0, 2, 9, 10, 11], [1, 0, 6, 8, 9], [15, 7, 0, 3, 8], [6, 8, 12, 0, 4], [5, 6, 9, 7, 0]]

# Parameters
num_ants = 10
num_iterations = 100
alpha = 1
beta = 5
rho = 0.8

# Initialize pheromone matrix
pheromones = [[1 / (num_cities * sum([row[i] for row in distances])) for j in range(num_cities)] for i in range(num_cities)]

for iteration in range(num_iterations):
    # Create ants
    ants = [random.randint(0, num_cities - 1) for i in range(num_ants)]
    for ant in ants:
        path = [ant]
        visited = [False for i in range(num_cities)]
        visited[ant] = True
        for i in range(num_cities - 1):
            next_city = -1
            denominator = 0
            for j in range(num_cities):
                if not visited[j]:
                    denominator += pheromones[path[-1]][j] ** alpha * (1 / distances[path[-1]][j]) ** beta
            for j in range(num_cities):
                if not visited[j]:
                    p = (pheromones[path[-1]][j] ** alpha * (1 / distances[path[-1]][j]) ** beta) / denominator
                    if p > random.random():
                        next_city = j
                        break
            if next_city == -1:
                for j in range(num_cities):
                    if not visited[j]:
                        next_city = j
                        break
            path.append(next_city)
            visited[next_city] = True
        # Update pheromones
        for i in range(num_cities - 1):
            pheromones[path[i]][path[i + 1]] += 1 / sum([distances[path[i]][path[j]] for j in range(i + 1, num_cities)])
            pheromones[path[i + 1]][path[i]] = pheromones[path[i]][path[i + 1]]
    # Evaporate pheromones
    for i in range(num_cities):
        for j in range(num_cities):
            pheromones[i][j] *= rho

# Find the best path
best_path = None
best_distance = None
for ant in ants:
    path = [ant]
    visited = [False for i in range(num_cities)]
    visited[ant] = True
    for i in range(num_cities - 1):
        next_city = -1
        denominator = 0
        for j in range(num_cities):
            if not visited[j]:
                denominator += pheromones[path[-1]][j] ** alpha * (1 / distances[path[-1]][j]) ** beta
        for j in range(num_cities):
            if not visited[j]:
                p = (pheromones[path[-1]][j] ** alpha * (1 / distances[path[-1]][j]) ** beta) / denominator
                if p > random.random():
                    next_city = j
                    break
        if next_city == -1:
            for j in range(num_cities):
                if not visited[j]:
                    next_city = j
                    break
        path.append(next_city)
        visited[next_city] = True
    distance = sum([distances[path[i]][path[i+1]] for i in range(num_cities-1)]) + distances[path[-1]][path[0]]
    if best_path is None or distance < best_distance:
        best_path = path
        best_distance = distance

# Print the results
print("Best path:", [i+1 for i in best_path])
print("Best distance:", best_distance)
