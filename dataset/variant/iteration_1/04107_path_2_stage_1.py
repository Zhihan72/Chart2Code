import matplotlib.pyplot as plt
import numpy as np

# Data representing fruit consumption on different planets
fruits = ['Apple', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Strawberry']
consumption_alpha = [15, 25, 10, 5, 30, 20]
consumption_beta = [20, 10, 15, 25, 10, 20]
consumption_gamma = [5, 20, 10, 30, 25, 10]
consumption_delta = [10, 15, 20, 25, 30, 5]
avg_sweetness_levels = [7, 5, 8, 6, 9, 7]

# Consolidate consumption data
data = []
for fruit, count in zip(fruits * 4, consumption_alpha + consumption_beta + consumption_gamma + consumption_delta):
    data.extend([fruit] * count)

# Setup the figure and axes for subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 6)) # Changed row and column arrangement

# Histogram representing fruit consumption on different planets
ax1 = axs[0]
n, bins, patches = ax1.hist(data, bins=len(fruits), edgecolor='black', color='skyblue', alpha=0.7)
ax1.set_title('Intergalactic Study of Alien Diets: Fruit Consumption on Different Planets', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Types of Fruits', fontsize=14)
ax1.set_ylabel('Number of Instances Consumed', fontsize=14)
ax1.set_xticks(np.arange(len(fruits)))
ax1.set_xticklabels(fruits)

for count, rect in zip(n, patches):
    height = rect.get_height()
    ax1.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

# Subplot representing average sweetness level of each fruit
ax2 = axs[1]
ax2.bar(fruits, avg_sweetness_levels, color='orchid', edgecolor='black', alpha=0.7)
ax2.set_title('Average Sweetness Levels of Different Fruits', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Types of Fruits', fontsize=14)
ax2.set_ylabel('Average Sweetness Level', fontsize=14)
ax2.set_ylim(0, 10) # Assuming sweetness level is on a scale of 0 to 10

# Adding annotations for sweetness levels
for i, sweetness in enumerate(avg_sweetness_levels):
    ax2.annotate(f'{sweetness}', xy=(i, sweetness),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()