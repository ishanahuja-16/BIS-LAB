import random
import math

# Define the function to maximize (example: f(x) = x * sin(10*pi*x) + 1)
def fitness_function(x):
    return x * math.sin(10 * math.pi * x) + 1

# Generate a random solution in the range
def random_solution(bounds):
    return random.uniform(bounds[0], bounds[1])

# Tournament selection
def selection(population, fitnesses):
    i, j = random.sample(range(len(population)), 2)
    return population[i] if fitnesses[i] > fitnesses[j] else population[j]

# Crossover (single-point for real values, blend here)
def crossover(p1, p2, crossover_rate):
    if random.random() < crossover_rate:
        return (p1 + p2) / 2
    return p1

# Mutation (small random change)
def mutate(solution, mutation_rate, bounds):
    if random.random() < mutation_rate:
        solution += random.uniform(-0.1, 0.1)
        solution = max(min(solution, bounds[1]), bounds[0])  # clamp to bounds
    return solution

def genetic_algorithm():
    # ===== USER INPUT =====
    print("Genetic Algorithm Optimization\n")
    population_size = int(input("Enter population size: "))
    generations = int(input("Enter number of generations: "))
    crossover_rate = float(input("Enter crossover rate (0-1): "))
    mutation_rate = float(input("Enter mutation rate (0-1): "))
    lower_bound = float(input("Enter lower bound of search space: "))
    upper_bound = float(input("Enter upper bound of search space: "))

    bounds = (lower_bound, upper_bound)

    # ===== Initialize Population =====
    population = [random_solution(bounds) for _ in range(population_size)]

    best_solution = population[0]
    best_fitness = fitness_function(best_solution)

    # ===== Evolution Process =====
    for gen in range(generations):
        fitnesses = [fitness_function(ind) for ind in population]

        # Track best
        for i, fit in enumerate(fitnesses):
            if fit > best_fitness:
                best_solution, best_fitness = population[i], fit

        new_population = []
        for _ in range(population_size):
            # Selection
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)

            # Crossover
            child = crossover(parent1, parent2, crossover_rate)

            # Mutation
            child = mutate(child, mutation_rate, bounds)

            new_population.append(child)

        population = new_population

        print(f"Generation {gen+1}: Best Solution = {best_solution:.5f}, Fitness = {best_fitness:.5f}")

    print("\n=== Final Best Solution ===")
    print(f"X = {best_solution:.5f}, Fitness = {best_fitness:.5f}")

# Run the algorithm
if __name__ == "__main__":
    genetic_algorithm()
