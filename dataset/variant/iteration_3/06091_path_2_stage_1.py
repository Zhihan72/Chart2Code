import matplotlib.pyplot as plt
import numpy as np

# Decades
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Number of butterflies spotted at different points
key_point_1 = np.array([1500, 1200, 900, 800, 1100])
key_point_2 = np.array([3000, 2800, 2500, 2400, 3000])
key_point_3 = np.array([2500, 2200, 1900, 1800, 2600])
key_point_4 = np.array([2000, 1800, 1500, 1400, 2000])

# Conservation efforts effectiveness
conservation_efforts = np.array([20, 40, 60, 80, 90])

# Create subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data
ax.plot(decades, key_point_1, 'o-', label='KP1', color='blue')
ax.plot(decades, key_point_2, 's-', label='KP2', color='orange')
ax.plot(decades, key_point_3, '^-', label='KP3', color='green')
ax.plot(decades, key_point_4, 'd-', label='KP4', color='red')

# Twin axes for conservation efforts
ax2 = ax.twinx()
ax2.plot(decades, conservation_efforts, 'o--', color='purple', label='Conservation')

# Titles and labels
ax.set_title('Monarchs (1980-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Butterflies Spotted', fontsize=12)
ax2.set_ylabel('Conservation (%)', fontsize=12, color='purple')

# Legend and grid
ax.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

# Annotate points
for decade, kp1, kp2, kp3, kp4 in zip(decades, key_point_1, key_point_2, key_point_3, key_point_4):
    ax.text(decade, kp1 + 100, f'{kp1}', ha='center', fontsize=9, color='blue')
    ax.text(decade, kp2 + 100, f'{kp2}', ha='center', fontsize=9, color='orange')
    ax.text(decade, kp3 + 100, f'{kp3}', ha='center', fontsize=9, color='green')
    ax.text(decade, kp4 + 100, f'{kp4}', ha='center', fontsize=9, color='red')

for decade, ce in zip(decades, conservation_efforts):
    ax2.text(decade, ce - 10, f'{ce}%', ha='center', fontsize=9, color='purple')

# Use tight layout
plt.tight_layout()

# Show plot
plt.show()