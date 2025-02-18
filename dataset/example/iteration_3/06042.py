import matplotlib.pyplot as plt
import numpy as np

# Backstory: Studying the relationship between hours of sleep, coffee consumption, and productivity among software developers.
# Data: Sleep hours, coffee cups, and productivity scores among developers.
sleep_hours = np.array([5, 6, 7, 8, 9, 10])
coffee_cups = np.array([4, 3, 3, 2, 2, 1])
productivity_scores = np.array([60, 65, 70, 80, 85, 90])

# Data: Highlighting physical activity levels impacting productivity scores.
activity_levels = np.array([1, 0.8, 0.9, 0.7, 0.85, 0.95])  # A normalized scale from 0 to 1

# Create figure and scatter plot
fig, ax1 = plt.subplots(figsize=(12, 8))

scatter = ax1.scatter(
    sleep_hours, 
    productivity_scores, 
    c=coffee_cups, 
    cmap='plasma', 
    s=100 * activity_levels,  # Size of points proportional to activity levels
    edgecolor='k', 
    alpha=0.7
)

# Add color bar for coffee consumption
cbar = plt.colorbar(scatter)
cbar.set_label('Cups of Coffee', fontsize=12)

# Customize axes and labels
ax1.set_title('Impact of Sleep, Coffee, and Physical Activity on Developer Productivity', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Hours of Sleep', fontsize=12)
ax1.set_ylabel('Productivity Score (out of 100)', fontsize=12)
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Adding trend line
z = np.polyfit(sleep_hours, productivity_scores, 1)
p = np.poly1d(z)
ax1.plot(sleep_hours, p(sleep_hours), "r--", linewidth=2, label="Trendline")

# Secondary y-axis for activity levels
ax2 = ax1.twinx()
ax2.plot(sleep_hours, activity_levels, color='green', marker='o', linestyle='-', label='Activity Level')
ax2.set_ylabel('Physical Activity Level', fontsize=12, color='green')

# Add legends
ax1.legend(loc='lower right')
ax2.legend(loc='upper left')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()