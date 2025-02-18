import matplotlib.pyplot as plt
import numpy as np

days = ["Funday", "Bluesday", "Humpday", "Thirstday", "Fryday", "Caturday", "Snoozeday"]
hours_of_coding_shuffled = np.array([8, 5, 9, 4, 7, 3, 6])
caffeine_consumption_shuffled = np.array([4, 2, 5, 2, 3, 1, 3])
tiredness_level_shuffled = np.array([7, 4, 8, 3, 6, 2, 5])
marker_sizes_shuffled = tiredness_level_shuffled * 20

shuffled_colors = np.array([
    plt.cm.magma(0.1),
    plt.cm.magma(0.5),
    plt.cm.magma(0.9),
    plt.cm.magma(0.6),
    plt.cm.magma(0.8),
    plt.cm.magma(0.7),
    plt.cm.magma(0.2)
])

# Changed figure size and scatter plot settings
plt.figure(figsize=(10, 5))
plt.scatter(hours_of_coding_shuffled, caffeine_consumption_shuffled, s=marker_sizes_shuffled, c=shuffled_colors, alpha=0.6, edgecolors='red', linewidth=1.5, marker='^')

# Adjusted text settings
for i, day in enumerate(days):
    plt.text(hours_of_coding_shuffled[i], caffeine_consumption_shuffled[i] + 0.3, day, fontsize=8, ha='right', color='purple')

# Changed grid and borders
plt.title('Geek Time vs. Coffee Intake\nMax Week Observations', fontsize=14, fontweight='light', color='teal')
plt.xlabel('Geek Hours/Day', fontsize=10, color='darkred')
plt.ylabel('Coffee Cups/Day', fontsize=10, color='darkred')
plt.grid(True, linestyle=':', linewidth=0.8, alpha=0.5)

# Updated legend style
handles = [plt.Line2D([0], [0], marker='^', color='w', markerfacecolor=shuffled_colors[i], markersize=8, label=days[i]) for i in range(len(days))]
plt.legend(title='Weekdays', handles=handles, loc='upper left', fontsize=8)
plt.tight_layout()

# Display the plot
plt.show()