import random
import matplotlib.pyplot as plt

# Define the total number of IP addresses and the number of vulnerable computers
TOTAL_IPS = 50000
VULNERABLE_COMPUTERS = set(range(1, 11)).union(set(range(1001, 1011))).union(set(range(2001, 2011)))
for i in range(4, 50):
    VULNERABLE_COMPUTERS = VULNERABLE_COMPUTERS.union(set(range(i * 1000 + 1, i * 1000 + 11)))
NON_VULNERABLE_COMPUTERS = set(range(1, TOTAL_IPS + 1)) - VULNERABLE_COMPUTERS

# Define the initial infected computer
INITIAL_INFECTED_COMPUTER = 2010

# Define the scan rate of the worm
SCAN_RATE = 4

# Define the number of simulation runs
NUM_RUNS = 3


# Define the function that simulates the worm propagation
def simulate_worm_propagation(scan_rate):
    # Initialize the infected computers set and the time variable
    infected_computers = {INITIAL_INFECTED_COMPUTER}
    time = 0
    time_step = []
    num_infected = []
    while len(infected_computers) < len(VULNERABLE_COMPUTERS):
        # Generate the list of IP addresses to scan
        ips_to_scan = []
        for infected_computer in infected_computers:
            for _ in range(scan_rate):
                ip_to_scan = random.randint(1, TOTAL_IPS)
                while ip_to_scan in infected_computers or ip_to_scan in ips_to_scan:
                    ip_to_scan = random.randint(1, TOTAL_IPS)
                ips_to_scan.append(ip_to_scan)
        # Check if any of the scanned IP addresses are vulnerable
        for ip_to_scan in ips_to_scan:
            if ip_to_scan in VULNERABLE_COMPUTERS:
                infected_computers.add(ip_to_scan)
        # Update the time variable
        time += 1
        time_step.append(time)
        num_infected.append(len(infected_computers))
    return time_step, num_infected


# Simulate the worm propagation for the specified number of runs
simulation_results = []
for i in range(NUM_RUNS):
    print("Simulation ", (i + 1))
    time, infected = simulate_worm_propagation(SCAN_RATE)
    simulation_results.append((time, infected))
    print(f"Finished in {time[-1]} time units\n")

# Plot the simulation results
plt.figure(figsize=(10, 6))
plt.xlabel('Time')
plt.ylabel('Number of Infected Computers')
plt.title('Worm Propagation Simulation')
colors = ['red', 'green', 'blue']
linestyles = ['solid', 'dashed', 'dotted']
for i, (time, infected) in enumerate(simulation_results):
    plt.plot(time, infected, label=f'Simulation {i+1}', color=colors[i], linestyle=linestyles[i])
plt.legend()
plt.savefig('random.png')
