import matplotlib.pyplot as plt
import numpy as np

# Data
sleep_hours = np.array([5, 6, 7, 8, 9, 10])
coffee_cups = np.array([4, 3, 3, 2, 2, 1])
productivity_scores = np.array([60, 65, 70, 80, 85, 90])
activity_levels = np.array([1, 0.8, 0.9, 0.7, 0.85, 0.95])

# Create figure and scatter plot
fig, ax1 = plt.subplots(figsize=(10, 6))

scatter = ax1.scatter(
    sleep_hours, 
    productivity_scores, 
    c=coffee_cups, 
    cmap='spring', 
    s=150 * activity_levels,  # Increased size proportional to activity levels
    edgecolor='gray', 
    alpha=0.8
)

# Add color bar for coffee consumption
cbar = plt.colorbar(scatter)
cbar.set_label('Coffee Intake (cups)', fontsize=11, style='italic')

# Customize axes and labels
ax1.set_title('Sleep vs. Productivity: Coffee & Activity Influence', fontsize=14, style='italic', color='darkblue')
ax1.set_xlabel('Sleep Duration (hours)', fontsize=11, color='darkred')
ax1.set_ylabel('Productivity Score', fontsize=11, color='darkgreen')
ax1.grid(visible=True, linestyle='-', alpha=0.3)

# Adding trend line with different style
z = np.polyfit(sleep_hours, productivity_scores, 1)
p = np.poly1d(z)
ax1.plot(sleep_hours, p(sleep_hours), "b-.", linewidth=1.5, label="Productivity Trend")

# Secondary y-axis for activity levels
ax2 = ax1.twinx()
ax2.plot(sleep_hours, activity_levels, color='purple', marker='s', linestyle='--', label='Activity Level')
ax2.set_ylabel('Activity Level', fontsize=11, color='purple')

# Add legends in different positions
ax1.legend(loc='upper left')
ax2.legend(loc='lower right')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()