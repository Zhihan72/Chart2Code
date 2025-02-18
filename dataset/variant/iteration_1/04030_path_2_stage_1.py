import matplotlib.pyplot as plt
import numpy as np

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours_of_coding = np.array([5, 6, 8, 7, 9, 4, 3])  # Hours of coding each day
caffeine_consumption = np.array([2, 3, 4, 3, 5, 2, 1])  # Cups of coffee/tea each day
tiredness_level = np.array([4, 5, 7, 6, 8, 3, 2])
marker_sizes = tiredness_level * 20
colors = plt.cm.viridis(np.linspace(0, 1, len(days)))

plt.figure(figsize=(12, 7))
plt.scatter(hours_of_coding, caffeine_consumption, s=marker_sizes, c=colors, alpha=0.8, edgecolors='black', linewidth=1, cmap='viridis')

for i, day in enumerate(days):
    plt.text(hours_of_coding[i], caffeine_consumption[i] + 0.2, day, fontsize=9, ha='center', color='darkblue')

plt.title('Coding Hours vs. Caffeine Consumption\nTracking Developer Habits Across a Week', fontsize=16, fontweight='bold')
plt.xlabel('Hours of Coding per Day', fontsize=12)
plt.ylabel('Cups of Caffeine Consumed per Day', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

plt.show()