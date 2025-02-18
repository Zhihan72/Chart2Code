import matplotlib.pyplot as plt
import numpy as np

cities = ['New York', 'Tokyo', 'London', 'Sydney', 'Berlin', 'Paris', 'São Paulo', 'Mumbai', 'Cairo', 'Beijing']
coffee_consumption = [300, 250, 280, 200, 220, 240, 180, 160, 220, 210]

fig, ax = plt.subplots(figsize=(14, 8))

# Shuffled colors list
colors = ['#33FF57', '#3357FF', '#F333FF', '#FF5733', '#FF33C4', '#33FFC4', '#FF3364', '#33F3FF', '#FF9633', '#3367FF']

bars = ax.bar(cities, coffee_consumption, color=colors, edgecolor='black')

for bar, consumption in zip(bars, coffee_consumption):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{consumption}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.set_title('Monthly Coffee Consumption by City\nAnalysis of Coffee Consumption Patterns Around the World', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Cities', fontsize=12, labelpad=10)
ax.set_ylabel('Average Cups of Coffee per Month', fontsize=12, labelpad=10)

ax.set_xticks(np.arange(len(cities)))
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=11)

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()