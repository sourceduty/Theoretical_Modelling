# Technological Relativity Simulation V1.0
# A visual representation of how the principles of Technological Relativity interact.

import numpy as np
import matplotlib.pyplot as plt

# Parameters
time_steps = 50
hubs = ["Hub A", "Hub B", "Hub C"]
initial_resources = [50, 30, 20]
gravity_effect = [1.2, 1.1, 1.05]
growth_rates = [0.05, 0.08, 0.1]
breakthrough_probabilities = [0.3, 0.5, 0.7]
saturation_limit = 100
plateau_point = 30
convergence_factor = 0.1

def simulate_resources_with_saturation(time_steps, initial_resources, gravity_effect, saturation_limit):
    resources = np.zeros((time_steps, len(initial_resources)))
    resources[0] = initial_resources
    for t in range(1, time_steps):
        resources[t] = resources[t - 1] * gravity_effect
        resources[t] = np.minimum(resources[t], saturation_limit)
    return resources

def simulate_technological_progress_with_plateau(time_steps, growth_rates, plateau_point):
    progress = np.zeros((time_steps, len(growth_rates)))
    progress[0] = [np.exp(rate * 0) for rate in growth_rates]
    for t in range(1, time_steps):
        if t < plateau_point:
            progress[t] = progress[t - 1] * np.exp([rate * 1 for rate in growth_rates])
        else:
            progress[t] = progress[t - 1] + [0.01 * p for p in progress[t - 1]]
    return progress

def simulate_breakthroughs_with_convergence(time_steps, breakthrough_probabilities, convergence_factor):
    breakthroughs = np.zeros((len(breakthrough_probabilities), time_steps))
    for t in range(1, time_steps):
        for i, prob in enumerate(breakthrough_probabilities):
            adjusted_prob = prob + convergence_factor * np.sum(breakthroughs[:, t - 1])
            if np.random.rand() < min(adjusted_prob, 1.0):
                breakthroughs[i, t] = breakthroughs[i, t - 1] + 1
            else:
                breakthroughs[i, t] = breakthroughs[i, t - 1]
    return breakthroughs

def plot_results(resources, progress, perceived_progress, breakthroughs, hubs, time_steps):
    plt.figure(figsize=(10, 6))
    for i, hub in enumerate(hubs):
        plt.plot(range(time_steps), resources[:, i], label=hub)
    plt.title('Technological Gravity Effect (Resources Over Time)')
    plt.xlabel('Time Steps')
    plt.ylabel('Resources')
    plt.legend()
    plt.grid()
    plt.savefig('Technological_Gravity.png')
    plt.close()

    plt.figure(figsize=(10, 6))
    for i, hub in enumerate(hubs):
        plt.plot(range(time_steps), progress[:, i], label=f'{hub} Actual Progress')
        plt.plot(range(time_steps), perceived_progress[:, i], linestyle='--', label=f'{hub} Perceived Progress')
    plt.title('Technological Progress with Length Contraction')
    plt.xlabel('Time Steps')
    plt.ylabel('Progress')
    plt.legend()
    plt.grid()
    plt.savefig('Technological_Progress.png')
    plt.close()

    plt.figure(figsize=(10, 6))
    for i, hub in enumerate(hubs):
        plt.step(range(time_steps), breakthroughs[i], label=f'{hub} Breakthroughs')
    plt.title('Breakthroughs (Technological Causality)')
    plt.xlabel('Time Steps')
    plt.ylabel('Number of Breakthroughs')
    plt.legend()
    plt.grid()
    plt.savefig('Technological_Breakthroughs.png')
    plt.close()

if __name__ == "__main__":
    resources = simulate_resources_with_saturation(time_steps, initial_resources, gravity_effect, saturation_limit)
    progress = simulate_technological_progress_with_plateau(time_steps, growth_rates, plateau_point)
    perceived_progress = progress / (1 + np.arange(1, time_steps + 1).reshape(-1, 1))
    breakthroughs = simulate_breakthroughs_with_convergence(time_steps, breakthrough_probabilities, convergence_factor)
    plot_results(resources, progress, perceived_progress, breakthroughs, hubs, time_steps)