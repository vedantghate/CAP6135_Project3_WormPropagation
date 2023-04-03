import random
import matplotlib.pyplot as plt

# Vulnerable computers' IP addresses
vulnerable_ips = []
initial_infected_ip = 2010

for i in range(0, 500, 10):
    for j in range(i + 1, i + 11):
        vulnerable_ips.append(j)
        if j == 2010:
            initial_infected_ip = j


# Define function to simulate worm propagation
def simulate_worm_propagation(scan_rate, sequential_probability):
    # Initialize variables
    infected_ips = [initial_infected_ip]
    sequential_ips = []
    random_ips = []
    for i in range(1, 500):
        if random.random() < sequential_probability:
            sequential_ips.append(vulnerable_ips[i])
        else:
            random_ips.append(vulnerable_ips[i])
    time_steps_in = [0]
    num_infected_in = [1]

    # Simulate worm propagation until all vulnerable computers are infected
    while len(infected_ips) < 500:
        newly_infected_ips = []
        for infected_ip in infected_ips:
            if infected_ip in sequential_ips:
                target_ip = (infected_ip % 50000) + 1
                if target_ip in vulnerable_ips and target_ip not in infected_ips:
                    newly_infected_ips.append(target_ip)
            else:
                for i in range(scan_rate):
                    target_ip = random.randint(1, 50000)
                    if target_ip in vulnerable_ips and target_ip not in infected_ips:
                        newly_infected_ips.append(target_ip)
        infected_ips += newly_infected_ips
        time_steps_in.append(time_steps_in[-1] + 1)
        num_infected_in.append(len(infected_ips))

    return time_steps_in, num_infected_in


# Run simulations and store results
simulations = []
for i in range(3):
    sequential_prob = 0.7
    if random.random() < 0.3:
        sequential_prob = 0.3
    time_steps, num_infected = simulate_worm_propagation(4, sequential_prob)
    simulations.append((time_steps, num_infected))

# Print time for all vulnerable computers to be infected in each simulation
for i, sim in enumerate(simulations):
    time_steps, num_infected = sim
    finish_time = time_steps[-1]
    print(f"Simulation {i + 1} finish time: {finish_time}")

# Plot results
fig, ax = plt.subplots()
colors = ['red', 'green', 'blue']
linestyles = ['solid', 'dashed', 'dotted']
for i, sim in enumerate(simulations):
    time_steps, num_infected = sim
    ax.plot(time_steps, num_infected, label=f"Simulation {i + 1}", color=colors[i], linestyle=linestyles[i])
ax.set_xlabel("Time")
ax.set_ylabel("Number of Infected Computers")
ax.legend()
plt.savefig('sequential.png')
