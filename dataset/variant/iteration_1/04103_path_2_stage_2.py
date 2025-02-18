import matplotlib.pyplot as plt
import numpy as np

# Time in months
time = np.arange(0, 101, 10)

# Distance in millions of kilometers including additional celestial bodies
distance_to_planets = {
    'Earth': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Mars': [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
    'Jupiter': [0, 100, 200, 300, 400, 500, 650, 800, 950, 1100, 1250],
    'Saturn': [0, 150, 300, 450, 600, 750, 950, 1150, 1350, 1550, 1750],
    'Neptune': [0, 200, 400, 600, 800, 1000, 1250, 1500, 1750, 2000, 2250],
    'Alpha': [0, 75, 150, 225, 300, 375, 450, 525, 600, 675, 750],
    'Beta': [0, 125, 250, 375, 500, 625, 750, 875, 1000, 1125, 1250],
    'Gamma': [0, 180, 360, 540, 720, 900, 1080, 1260, 1440, 1620, 1800]
}

# Shuffled color assignment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6', '#c2c2f0', '#ff6666', '#c2f0c2']

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each celestial body's flight path with shuffled colors
for (body, distances), color in zip(distance_to_planets.items(), colors):
    ax.plot(time, distances, label=body, marker='o', linestyle='-', linewidth=2, alpha=0.7, color=color)

# Title and labels
ax.set_title('Voyager X: Journey Across the Solar System and Beyond', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time (Months)', fontsize=12)
ax.set_ylabel('Distance from Earth (Million km)', fontsize=12)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Legend
ax.legend(fontsize=12, loc='upper left')

# Annotations for original planets
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