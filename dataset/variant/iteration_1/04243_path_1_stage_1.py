import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.array([2025, 2030, 2035, 2040, 2045, 2050])

# Temperatures for different Martian colonies (in degrees Celsius)
colony_A = np.array([-70, -65, -60, -55, -50, -45])
colony_B = np.array([-68, -63, -58, -53, -47, -42])
colony_C = np.array([-72, -67, -62, -58, -52, -48])
colony_D = np.array([-69, -64, -61, -56, -50, -46])

# Additional colonies data
colony_E = np.array([-71, -66, -59, -54, -48, -43])
colony_F = np.array([-73, -69, -63, -57, -51, -47])

# Setting up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot for Colony A
ax.plot(years, colony_A, label='Colony A', color='firebrick', marker='o', linestyle='-', linewidth=2, markersize=8)

# Plot for Colony B
ax.plot(years, colony_B, label='Colony B', color='skyblue', marker='s', linestyle='-', linewidth=2, markersize=8)

# Plot for Colony C
ax.plot(years, colony_C, label='Colony C', color='seagreen', marker='^', linestyle='-', linewidth=2, markersize=8)

# Plot for Colony D
ax.plot(years, colony_D, label='Colony D', color='orchid', marker='D', linestyle='-', linewidth=2, markersize=8)

# Plot for Colony E
ax.plot(years, colony_E, label='Colony E', color='gold', marker='x', linestyle='-', linewidth=2, markersize=8)

# Plot for Colony F
ax.plot(years, colony_F, label='Colony F', color='darkorange', marker='*', linestyle='-', linewidth=2, markersize=8)

# Title and labels
ax.set_title("Average Temperature Evolution in Martian Colonies (2025-2050)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Temperature (°C)", fontsize=14)

# Adding legend
ax.legend(title="Martian Colonies", fontsize=12, title_fontsize=14, loc='lower left')

# Adding grid
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()