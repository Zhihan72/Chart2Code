import matplotlib.pyplot as plt
import numpy as np

# Day numbers (1 through 30)
days = np.arange(1, 31)

# Fictional Data
# Exercise Intensity (arbitrary units)
exercise_intensity = np.array([
    3, 4, 5, 6, 7, 6, 5, 6, 7, 8, 7, 6, 5, 7, 8, 7, 6, 5, 6, 7, 6, 5, 6, 7, 
    8, 7, 6, 5, 4, 3
])

# Plotting setup
fig, ax = plt.subplots(figsize=(14, 7))

# Exercise Intensity Line Plot
ax.plot(days, exercise_intensity, color='green', marker='o', linewidth=2, markersize=8, label='Exercise Intensity')

# Titles and Labels
ax.set_title('30-Day Fitness Challenge: Exercise Intensity', fontsize=18, fontweight='bold')
ax.set_xlabel('Days', fontsize=14)
ax.set_ylabel('Exercise Intensity (arbitrary units)', fontsize=14, color='green')

# Grid for clarity
ax.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)

# Legend
ax.legend(loc='upper left', fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()