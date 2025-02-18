import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
days = np.arange(1, 31)
exercise_intensity = np.array([
    3, 4, 5, 6, 7, 6, 5, 6, 7, 8, 7, 6, 5, 7, 8, 7, 6, 5, 6, 7, 6, 5, 6, 7, 
    8, 7, 6, 5, 4, 3
])
heart_rate_recovery = np.array([
    20, 18, 19, 17, 16, 17, 18, 17, 16, 15, 16, 17, 18, 16, 15, 16, 17, 18, 
    17, 16, 17, 18, 17, 16, 15, 16, 17, 18, 19, 20
])

# Create subplot
fig, ax = plt.subplots(figsize=(14, 7))

# Plot exercise intensity with different style
ax.plot(days, exercise_intensity, color='blue', marker='s', linewidth=1.5, markersize=10)
ax2 = ax.twinx()

# Plot heart rate recovery with different style
ax2.plot(days, heart_rate_recovery, color='green', marker='^', linestyle='-.', linewidth=1.5, markersize=7)

# Add grid with different style
ax.grid(visible=True, linestyle=':', linewidth=1, alpha=0.5)

# Add titles and legend for context
ax.set_title("Exercise Intensity and Heart Rate Recovery Over Days")
ax.set_xlabel("Days")
ax.set_ylabel("Exercise Intensity")
ax2.set_ylabel("Heart Rate Recovery")

# Add legend to describe the plot lines
ax.legend(['Exercise Intensity'], loc='upper left')
ax2.legend(['Heart Rate Recovery'], loc='upper right')

# Adjust layout to avoid clipping
plt.tight_layout()

# Display the plot
plt.show()