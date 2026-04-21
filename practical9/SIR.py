import numpy as np
import matplotlib.pyplot as plt
N = 10000
S = 9999
I = 1
R = 0
beta = 0.3
gamma = 0.05
S_values = [S]
I_values = [I]
R_values = [R]
time_points = [0]
for t in range(1, 1001):
    infection_prob = beta * (I / N)
    if infection_prob > 1:
        infection_prob = 1
    if S > 0:
        new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
    else:
        new_infections = 0
    if I > 0:
        new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
    else:
        new_recoveries = 0
    if new_infections > S:
        new_infections = S
    if new_recoveries > I:
        new_recoveries = I
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries
    time_points.append(t)
    S_values.append(S)
    I_values.append(I)
    R_values.append(R)
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(time_points, S_values, label="susceptible")
plt.plot(time_points, I_values, label="infected")
plt.plot(time_points, R_values, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.savefig("SIR_plot.png")
plt.show()