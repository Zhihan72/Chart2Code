import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the relationship between hours of coding and caffeine consumption among developers throughout a week.
# 

# Data for hours of coding throughout a week (same sequence for easier matching)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours_of_coding = np.array([5, 6, 8, 7, 9, 4, 3])  # Hours of coding each day

# Data for caffeine intake for the same week
caffeine_consumption = np.array([2, 3, 4, 3, 5, 2, 1])  # Cups of coffee/tea each day

# Illustrate feeling tiredness level annotated on the chart (scale 1 to 10)
tiredness_level = np.array([4, 5, 7, 6, 8, 3, 2])

# Customize marker sizes based on tiredness levels
marker_sizes = tiredness_level * 20

# Colors based on the days of the week using a colormap
colors = plt.cm.viridis(np.linspace(0, 1, len(days)))

# Create a figure
plt.figure(figsize=(12, 7))

# Scatter plot: Hours of coding vs caffeine consumption
plt.scatter(hours_of_coding, caffeine_consumption, s=marker_sizes, c=colors, alpha=0.8, edgecolors='black', linewidth=1, cmap='viridis')

# Adding labels to each point
for i, day in enumerate(days):
    plt.text(hours_of_coding[i], caffeine_consumption[i] + 0.2, day, fontsize=9, ha='center', color='darkblue')

# Title and labels
plt.title('Coding Hours vs. Caffeine Consumption\nTracking Developer Habits Across a Week', fontsize=16, fontweight='bold')
plt.xlabel('Hours of Coding per Day', fontsize=12)
plt.ylabel('Cups of Caffeine Consumed per Day', fontsize=12)

# Adding grid
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Legend using proxy artists for days of the week
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[i], markersize=8, label=days[i]) for i in range(len(days))]
plt.legend(title='Days of the Week', handles=handles, loc='best', fontsize=9)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()