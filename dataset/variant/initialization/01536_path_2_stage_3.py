import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
years = np.arange(2010, 2020)
strawberries_yield = np.array([1.0, 1.2, 1.5, 2.0, 2.2, 2.4, 2.8, 3.0, 3.5, 3.8])
tomatoes_yield = np.array([1.5, 1.7, 1.8, 2.1, 2.4, 2.6, 3.0, 3.2, 3.4, 3.9])

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting stacked areas
ax.fill_between(years, strawberries_yield, color='#FF6347', alpha=0.6)
ax.fill_between(years, strawberries_yield + tomatoes_yield, strawberries_yield, color='#FFD700', alpha=0.6)

# Titles and labels
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Yield (T)', fontsize=12)

# Beautify x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 12, 1))
ax.yaxis.set_tick_params(labelsize=10)
ax.xaxis.set_tick_params(labelsize=10)

# Avoid overlapping x-axis labels
plt.xticks(rotation=45)

# Tidy layout to prevent clipping
plt.tight_layout()

# Show plot
plt.show()