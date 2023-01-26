import random

# Parameters
POPULATION_SIZE = 50
MAX_GENERATION = 50
POPULATION_MUTATION = 0.1

# OneMax function
def oneMax(individual):
    return sum(individual),

# Initialize population
population = [[random.randint(0, 1) for _ in range(100)] for _ in range(POPULATION_SIZE)]

# Evolution loop
for generation in range(MAX_GENERATION):
    # Evaluate population
    fitness_values = [oneMax(individual) for individual in population]

    # Select parents
    parents = [population[i] for i in range(POPULATION_SIZE) if fitness_values[i] == max(fitness_values)]
    
    # Create offspring
    offspring = parents.copy()
    for i in range(POPULATION_SIZE - len(parents)):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = parent1.copy()
        for j in range(len(child)):
            if random.uniform(0, 1) < POPULATION_MUTATION:
                child[j] = int(not child[j])
        offspring.append(child)
    
    population = offspring
    print("Generation: ", generation, " Best individual: ", oneMax(parents[0]), " Fitness: ", max(fitness_values))

print("Final best individual: ", parents[0], " Fitness: ", oneMax(parents[0]))
