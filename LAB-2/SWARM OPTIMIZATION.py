import random

# Sphere function to minimize
def sphere_function(position):
    return sum([x**2 for x in position])

# Particle class
class Particle:
    def __init__(self, num_dimensions):
        self.position = [random.uniform(-10, 10) for _ in range(num_dimensions)]
        self.velocity = [random.uniform(-1, 1) for _ in range(num_dimensions)]
        self.best_position = list(self.position)
        self.best_fitness = sphere_function(self.position)

    def update_velocity(self, global_best_position, w, c1, c2):
        for i in range(len(self.position)):
            r1 = random.random()
            r2 = random.random()
            cognitive = c1 * r1 * (self.best_position[i] - self.position[i])
            social = c2 * r2 * (global_best_position[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + cognitive + social

    def update_position(self):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

    def evaluate(self):
        fitness = sphere_function(self.position)
        if fitness < self.best_fitness:
            self.best_fitness = fitness
            self.best_position = list(self.position)

# PSO algorithm
def pso(num_particles, num_dimensions, max_iter, w, c1, c2):
    swarm = [Particle(num_dimensions) for _ in range(num_particles)]

    global_best_position = list(swarm[0].best_position)
    global_best_fitness = swarm[0].best_fitness

    for particle in swarm:
        if particle.best_fitness < global_best_fitness:
            global_best_fitness = particle.best_fitness
            global_best_position = list(particle.best_position)

    for iteration in range(max_iter):
        for particle in swarm:
            particle.update_velocity(global_best_position, w, c1, c2)
            particle.update_position()
            particle.evaluate()

            if particle.best_fitness < global_best_fitness:
                global_best_fitness = particle.best_fitness
                global_best_position = list(particle.best_position)

        print(f"Iteration {iteration+1}/{max_iter}, Best Fitness: {global_best_fitness:.6f}")

    return global_best_position, global_best_fitness

# Get inputs from user
def get_user_inputs():
    print("Particle Swarm Optimization for Function Minimization\n")
    num_particles = int(input("Enter number of particles (e.g. 30): "))
    num_dimensions = int(input("Enter number of dimensions (e.g. 2): "))
    max_iter = int(input("Enter number of iterations (e.g. 100): "))
    w = float(input("Enter inertia weight w (e.g. 0.7): "))
    c1 = float(input("Enter cognitive coefficient c1 (e.g. 1.5): "))
    c2 = float(input("Enter social coefficient c2 (e.g. 1.5): "))
    return num_particles, num_dimensions, max_iter, w, c1, c2

# Run the program
if __name__ == "__main__":
    num_particles, num_dimensions, max_iter, w, c1, c2 = get_user_inputs()
    best_position, best_fitness = pso(num_particles, num_dimensions, max_iter, w, c1, c2)

    print("\n=== Optimization Result ===")
    print("Best Position Found:", ['{:.6f}'.format(x) for x in best_position])
    print("Best Fitness Value:", '{:.10f}'.format(best_fitness))
