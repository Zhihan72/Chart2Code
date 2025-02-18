import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2020)

fig, ax = plt.subplots(figsize=(12, 6))

# Set a different grid style
ax.grid(True, linestyle='-', alpha=0.3)

# Add arbitrary plot with different stylistic elements
example_values = np.random.uniform(800, 1300, size=years.size)  # Random data for illustration
ax.plot(years, example_values, color='purple', linewidth=1.5, linestyle='dotted', 
        marker='s', markersize=8, label='Example Data')

# Set random axis limits (but still reasonable)
ax.set_xlim(2000, 2020)
ax.set_ylim(800, 1300)

# Instantiate legend with a distinct location and style
ax.legend(loc='upper left', frameon=True, fontsize=10, borderpad=0.8)

# Customizing plot borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(True)

plt.tight_layout()
plt.show()