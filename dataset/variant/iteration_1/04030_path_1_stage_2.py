import matplotlib.pyplot as plt
import numpy as np

# Altered days of the week
days = ["Funday", "Bluesday", "Humpday", "Thirstday", "Fryday", "Caturday", "Snoozeday"]
hours_of_coding = np.array([5, 6, 8, 7, 9, 4, 3])
caffeine_consumption = np.array([2, 3, 4, 3, 5, 2, 1])
tiredness_level = np.array([4, 5, 7, 6, 8, 3, 2])
marker_sizes = tiredness_level * 20

shuffled_colors = np.array([
    plt.cm.viridis(0.5),
    plt.cm.viridis(0.9),
    plt.cm.viridis(0.1),
    plt.cm.viridis(0.8),
    plt.cm.viridis(0.2),
    plt.cm.viridis(0.6),
    plt.cm.viridis(0.7)
])

plt.figure(figsize=(12, 7))
plt.scatter(hours_of_coding, caffeine_consumption, s=marker_sizes, c=shuffled_colors, alpha=0.8, edgecolors='black', linewidth=1)

# Updated group labels for the days
for i, day in enumerate(days):
    plt.text(hours_of_coding[i], caffeine_consumption[i] + 0.2, day, fontsize=9, ha='center', color='darkblue')

# Randomly altered title and axis labels
plt.title('Geek Time vs. Coffee Intake\nObserving Coder Patterns Over Max Week', fontsize=16, fontweight='bold')
plt.xlabel('Geek Hours per Day', fontsize=12)
plt.ylabel('Coffee Cups Intake per Day', fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Legend with altered day labels
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=shuffled_colors[i], markersize=8, label=days[i]) for i in range(len(days))]
plt.legend(title='Craze of the Days', handles=handles, loc='best', fontsize=9)
plt.tight_layout()

plt.show()