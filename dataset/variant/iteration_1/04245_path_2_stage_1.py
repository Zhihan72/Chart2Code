import matplotlib.pyplot as plt
import numpy as np

# Time span in years
years = np.arange(1960, 2020, 10)

# Population data for Dragons in various regions
dragons_north = [150, 180, 220, 260, 240, 200]
dragons_east = [100, 130, 180, 220, 260, 300]
dragons_west = [80, 90, 130, 170, 160, 150]

# Population data for Unicorns in various regions
unicorns_north = [200, 210, 250, 280, 260, 240]
unicorns_east = [230, 270, 300, 310, 305, 290]
unicorns_west = [120, 150, 180, 210, 220, 230]

# Population data for Phoenixes in various regions
phoenixes_north = [50, 70, 90, 120, 150, 180]
phoenixes_east = [60, 80, 130, 170, 210, 250]
phoenixes_west = [40, 50, 60, 80, 110, 140]

# Additional Population data for Griffins in various regions
griffins_north = [30, 50, 70, 90, 120, 150]
griffins_east = [40, 60, 80, 110, 140, 170]
griffins_west = [20, 40, 60, 70, 90, 110]

# Function to create plots for a creature across regions
def plot_creature(ax, years, data_north, data_east, data_west, creature_name):
    ax.plot(years, data_north, label=f'{creature_name} - North', marker='o')
    ax.plot(years, data_east, label=f'{creature_name} - East', marker='s')
    ax.plot(years, data_west, label=f'{creature_name} - West', marker='^')
    ax.set_title(f'Population of {creature_name}', fontsize=14)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Population', fontsize=12)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)

# Set up the figure with 4x1 subplots
fig, axes = plt.subplots(4, 1, figsize=(12, 24))

# Plot each creature using the function
plot_creature(axes[0], years, dragons_north, dragons_east, dragons_west, 'Dragons')
plot_creature(axes[1], years, unicorns_north, unicorns_east, unicorns_west, 'Unicorns')
plot_creature(axes[2], years, phoenixes_north, phoenixes_east, phoenixes_west, 'Phoenixes')
plot_creature(axes[3], years, griffins_north, griffins_east, griffins_west, 'Griffins')

# Main title and layout adjustments
fig.suptitle('Population Trends of Mythical Creatures (1970-2020)', fontsize=20, fontweight='bold', y=0.92)
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()