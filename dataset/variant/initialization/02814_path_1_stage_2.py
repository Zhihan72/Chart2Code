import matplotlib.pyplot as plt
import numpy as np

# Define the decades
decades = ['1970s', '1980s', '1990s', '2000s', '2010s']

# Define the renewable energy types and their respective adoption data
solar_energy = np.array([5, 10, 15, 20, 25])
hydro_energy = np.array([8, 10, 13, 16, 20])

# Plotting the area chart with a single consistent color
fig, ax = plt.subplots(figsize=(12, 8))

# Use a single color for both datasets
consistent_color = '#FFD700'

# Plot areas with transparency
ax.fill_between(decades, solar_energy, color=consistent_color, alpha=0.6, label='Solar Energy')
ax.fill_between(decades, hydro_energy, color=consistent_color, alpha=0.6, label='Hydro Energy')

# Line plot to enhance trends
ax.plot(decades, solar_energy, color=consistent_color, linewidth=2)
ax.plot(decades, hydro_energy, color=consistent_color, linewidth=2)

# Title, labels, and legend
ax.set_title("Renewable Energy Adoption in Harmony\n(1970s-2010s)", fontsize=16, fontweight='bold')
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Energy Usage (Arbitrary Units)', fontsize=12)
ax.legend(loc='upper left', title="Energy Types", fontsize=10)

# Customize ticks and grid
ax.set_xticks(decades)
ax.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate the final points to highlight end values
for i, energy in enumerate([solar_energy, hydro_energy]):
    ax.annotate(
        str(energy[-1]),
        xy=(decades[-1], energy[-1]),
        xytext=(10, -10 * i),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', lw=1.5),
        fontsize=10,
        color='black'
    )

plt.tight_layout()
plt.show()