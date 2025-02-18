import matplotlib.pyplot as plt
import numpy as np

# Data setup
countries = ['Country A', 'Country B', 'Country C', 'Country D']
energy_types = ['Solar', 'Wind', 'Hydro']
percentage_distributions = np.array([
    [40, 35, 25],  # Country A
    [30, 40, 30],  # Country B
    [50, 20, 30],  # Country C
    [20, 50, 30]   # Country D
])

# Calculate total energy distribution per country
total_distribution = percentage_distributions.sum(axis=1)

# Sort countries by total energy distribution
sorted_indices = np.argsort(total_distribution)
sorted_countries = [countries[i] for i in sorted_indices]
sorted_distribution = percentage_distributions[sorted_indices]

# Plot parameters
x_positions = np.arange(len(energy_types))

fig, ax = plt.subplots(figsize=(10, 6))
for i in range(len(sorted_countries)):
    ax.bar(x_positions + (i * 0.2), sorted_distribution[i], width=0.2, 
           edgecolor='black', linestyle='--')

ax.set_xticks(x_positions + 0.3)
ax.set_ylim(0, max(total_distribution) + 15)

ax.grid(True, linestyle=':', linewidth=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()