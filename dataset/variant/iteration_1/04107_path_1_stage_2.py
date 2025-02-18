import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apple', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Strawberry']
consumption_alpha = [15, 25, 10, 5, 30, 20]
consumption_beta = [20, 10, 15, 25, 10, 20]
consumption_gamma = [5, 20, 10, 30, 25, 10]
avg_sweetness_levels = [7, 5, 8, 6, 9, 7]

data = []
for fruit, count in zip(fruits * 3, consumption_alpha + consumption_beta + consumption_gamma):
    data.extend([fruit] * count)

fig, axs = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [2, 1]})

ax1 = axs[0]
n, bins, patches = ax1.hist(data, bins=len(fruits), edgecolor='black', color='mediumseagreen', alpha=0.7)
ax1.set_title('Intergalactic Study of Alien Diets: Fruit Consumption on Different Planets', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Types of Fruits', fontsize=14)
ax1.set_ylabel('Number of Instances Consumed', fontsize=14)
ax1.set_xticks(np.arange(len(fruits)))
ax1.set_xticklabels(fruits)

for count, rect in zip(n, patches):
    height = rect.get_height()
    ax1.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

ax2 = axs[1]
ax2.bar(fruits, avg_sweetness_levels, color='tomato', edgecolor='black', alpha=0.7)
ax2.set_title('Average Sweetness Levels of Different Fruits', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Types of Fruits', fontsize=14)
ax2.set_ylabel('Average Sweetness Level', fontsize=14)
ax2.set_ylim(0, 10)

for i, sweetness in enumerate(avg_sweetness_levels):
    ax2.annotate(f'{sweetness}', xy=(i, sweetness),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()