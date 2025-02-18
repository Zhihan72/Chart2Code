import numpy as np
import matplotlib.pyplot as plt

# Setting the data for a backstory about planetary orbits
years = np.linspace(1, 12, 12)
# Planets around a star in a simulated exoplanet system
orbital_radius_planet_a = np.sin(years / 2) * 0.5 + 1
orbital_radius_planet_b = np.sin((years - 1) / 2) * 0.4 + 1.5
orbital_radius_planet_c = np.sin((years - 2) / 2) * 0.3 + 2

fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the data for Planet A
ax.plot(years, orbital_radius_planet_a, linestyle='-', marker='o', color='blue', label='Planet A')
# Plotting the data for Planet B
ax.plot(years, orbital_radius_planet_b, linestyle='-', marker='s', color='red', label='Planet B')
# Plotting the data for Planet C
ax.plot(years, orbital_radius_planet_c, linestyle='-', marker='^', color='green', label='Planet C')

# Adding title and labels
ax.set_title("Simulated Orbits of Planets A, B, and C over Time", fontsize=16, pad=20)
ax.set_xlabel("Years", fontsize=13)
ax.set_ylabel("Orbital Radius (AU)", fontsize=13)

# Adding a legend
ax.legend(loc='upper right', fontsize=12)

# Adding grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adding background
fig.patch.set_facecolor('#f0f0f0')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()