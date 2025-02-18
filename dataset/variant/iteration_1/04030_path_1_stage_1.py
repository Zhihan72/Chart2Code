import matplotlib.pyplot as plt
import numpy as np

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours_of_coding = np.array([5, 6, 8, 7, 9, 4, 3])
caffeine_consumption = np.array([2, 3, 4, 3, 5, 2, 1])
tiredness_level = np.array([4, 5, 7, 6, 8, 3, 2])
marker_sizes = tiredness_level * 20

# Original color sequence: Monday to Sunday
# colors = plt.cm.viridis(np.linspace(0, 1, len(days)))

# Manually shuffled colors for each day of the week
shuffled_colors = np.array([
    plt.cm.viridis(0.5),  # Shuffled Monday
    plt.cm.viridis(0.9),  # Shuffled Tuesday
    plt.cm.viridis(0.1),  # Shuffled Wednesday
    plt.cm.viridis(0.8),  # Shuffled Thursday
    plt.cm.viridis(0.2),  # Shuffled Friday
    plt.cm.viridis(0.6),  # Shuffled Saturday
    plt.cm.viridis(0.7)   # Shuffled Sunday
])

plt.figure(figsize=(12, 7))
plt.scatter(hours_of_coding, caffeine_consumption, s=marker_sizes, c=shuffled_colors, alpha=0.8, edgecolors='black', linewidth=1)

for i, day in enumerate(days):
    plt.text(hours_of_coding[i], caffeine_consumption[i] + 0.2, day, fontsize=9, ha='center', color='darkblue')

plt.title('Coding Hours vs. Caffeine Consumption\nTracking Developer Habits Across a Week', fontsize=16, fontweight='bold')
plt.xlabel('Hours of Coding per Day', fontsize=12)
plt.ylabel('Cups of Caffeine Consumed per Day', fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=shuffled_colors[i], markersize=8, label=days[i]) for i in range(len(days))]
plt.legend(title='Days of the Week', handles=handles, loc='best', fontsize=9)
plt.tight_layout()

plt.show()