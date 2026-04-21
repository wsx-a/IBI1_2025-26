import numpy as np
import matplotlib.pyplot as plt
population = np.zeros((100, 100), dtype=int)
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.3
gamma = 0.05
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap="viridis", interpolation="nearest")
plt.title("Spatial SIR at time 0")
plt.show()
for t in range(1, 101):
    new_population = population.copy()
    infected_points = np.where(population == 1)
    for k in range(len(infected_points[0])):
        x = infected_points[0][k]
        y = infected_points[1][k]
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:                
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy
                if 0 <= nx < 100 and 0 <= ny < 100:
                    if population[nx, ny] == 0:
                        if np.random.random() < beta:
                            new_population[nx, ny] = 1
        if np.random.random() < gamma:
            new_population[x, y] = 2

    population = new_population
    if t in [10, 50, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap="viridis", interpolation="nearest")
        plt.title("Spatial SIR at time " + str(t))
        plt.show()