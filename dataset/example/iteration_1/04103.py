import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This chart shows the journey of a spacecraft named "Voyager X" during its mission to explore different planets in our solar system. 
# The data represents the distance traveled by Voyager X from Earth to each planet over a period of time.

# Time in months
time = np.arange(0, 101, 10)

# Distance in millions of kilometers
distance_to_planets = {
    'Earth': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Mars': [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
    'Jupiter': [0, 100, 200, 300, 400, 500, 650, 800, 950, 1100, 1250],
    'Saturn': [0, 150, 300, 450, 600, 750, 950, 1150, 1350, 1550, 1750],
    'Neptune': [0, 200, 400, 600, 800, 1000, 1250, 1500, 1750, 2000, 2250]
}

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each planet's flight path
for planet, distances in distance_to_planets.items():
    ax.plot(time, distances, label=planet, marker='o', linestyle='-', linewidth=2, alpha=0.7)

# Title and labels
ax.set_title('Voyager X: Journey Across the Solar System', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time (Months)', fontsize=12)
ax.set_ylabel('Distance from Earth (Million km)', fontsize=12)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Legend
ax.legend(fontsize=12, loc='upper left')

# Annotations
ax.annotate('Mars Mission Completed', xy=(50, 500), xytext=(30, 700),
            arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)

ax.annotate('Jupiter Flyby', xy=(60, 650), xytext=(70, 800),
            arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)

ax.annotate('Saturn Ring Study', xy=(80, 1150), xytext=(50, 1350),
            arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)

# Ensure layout is tidy
fig.tight_layout()

# Show the plot
plt.show()