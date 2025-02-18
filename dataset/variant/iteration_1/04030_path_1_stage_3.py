import matplotlib.pyplot as plt
import numpy as np

# Altered days of the week
days = ["Funday", "Bluesday", "Humpday", "Thirstday", "Fryday", "Caturday", "Snoozeday"]

# Manually shuffled data arrays that maintain the original structure
hours_of_coding_shuffled = np.array([8, 5, 9, 4, 7, 3, 6])  # Random shuffling of original data
caffeine_consumption_shuffled = np.array([4, 2, 5, 2, 3, 1, 3])
tiredness_level_shuffled = np.array([7, 4, 8, 3, 6, 2, 5])
marker_sizes_shuffled = tiredness_level_shuffled * 20

# Corresponding shuffled colors
shuffled_colors = np.array([
    plt.cm.viridis(0.1),
    plt.cm.viridis(0.5),
    plt.cm.viridis(0.9),
    plt.cm.viridis(0.6),
    plt.cm.viridis(0.8),
    plt.cm.viridis(0.7),
    plt.cm.viridis(0.2)
])

plt.figure(figsize=(12, 7))
plt.scatter(hours_of_coding_shuffled, caffeine_consumption_shuffled, s=marker_sizes_shuffled, c=shuffled_colors, alpha=0.8, edgecolors='black', linewidth=1)

for i, day in enumerate(days):
    plt.text(hours_of_coding_shuffled[i], caffeine_consumption_shuffled[i] + 0.2, day, fontsize=9, ha='center', color='darkblue')

plt.title('Geek Time vs. Coffee Intake\nObserving Coder Patterns Over Max Week', fontsize=16, fontweight='bold')
plt.xlabel('Geek Hours per Day', fontsize=12)
plt.ylabel('Coffee Cups Intake per Day', fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=shuffled_colors[i], markersize=8, label=days[i]) for i in range(len(days))]
plt.legend(title='Craze of the Days', handles=handles, loc='best', fontsize=9)
plt.tight_layout()

plt.show()