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

# Altered color assignment for clear distinction
colors = ['#66b3ff', '#ff9999', '#c2f0c2', '#99ff99', '#ffb3e6', '#ffcc99', '#c2c2f0', '#ff6666']

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each celestial body's flight path with different styles
markers = ['o', '^', 's', 'D', 'x', '*', 'p', 'h']
linestyles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
for (body, distances), color, marker, linestyle in zip(distance_to_planets.items(), colors, markers, linestyles):
    ax.plot(time, distances, label=body, marker=marker, linestyle=linestyle, linewidth=2, alpha=0.8, color=color)

# Title and labels
ax.set_title('Voyager X: Journey Across the Solar System and Beyond', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time (Months)', fontsize=12)
ax.set_ylabel('Distance from Earth (Million km)', fontsize=12)

# Altered grid for aesthetics
ax.grid(True, linestyle=':', alpha=0.3)

# Legend with different positioning and style
ax.legend(fontsize=10, loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=4)

# Border adjustments
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Annotations for original planets
ax.annotate('Mars Mission Completed', xy=(50, 500), xytext=(20, 700),
            arrowprops=dict(facecolor='grey', arrowstyle='->', alpha=0.6), fontsize=11)

ax.annotate('Jupiter Flyby', xy=(60, 650), xytext=(70, 850),
            arrowprops=dict(facecolor='grey', arrowstyle='->', alpha=0.6), fontsize=11)

ax.annotate('Saturn Ring Study', xy=(80, 1150), xytext=(40, 1400),
            arrowprops=dict(facecolor='grey', arrowstyle='->', alpha=0.6), fontsize=11)

# Ensure layout is tidy
fig.tight_layout()

# Show the plot
plt.show()