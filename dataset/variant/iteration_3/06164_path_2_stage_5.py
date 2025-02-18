import matplotlib.pyplot as plt
import numpy as np

# Data
fruits = ['Apples', 'Bananas', 'Grapes']
consumption_data = [50, 30, 10]
calories_data = [2000, 1500, 300]

# Combine and sort data
sorted_data = sorted(zip(fruits, consumption_data, calories_data), key=lambda x: x[1], reverse=True)
fruits_sorted, consumption_sorted, calories_sorted = zip(*sorted_data)

fig, ax1 = plt.subplots(figsize=(14, 8))

x_pos = np.arange(len(fruits_sorted))
bar_width = 0.4

bars1 = ax1.bar(x_pos, consumption_sorted, width=bar_width, color='#6A5ACD', alpha=0.7)

ax2 = ax1.twinx()
bars2 = ax2.bar(x_pos + bar_width, calories_sorted, width=bar_width, color='#6A5ACD', alpha=0.7)

for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=10, color='#6A5ACD')

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center', va='bottom', fontsize=10, color='#6A5ACD')

plt.title('Fruit Stats 2023', fontsize=16, fontweight='bold')
ax1.set_xlabel('Types', fontsize=12)
ax1.set_ylabel('Avg. Cons.', fontsize=12, color='#6A5ACD')
ax2.set_ylabel('Calories', fontsize=12, color='#6A5ACD')

ax1.set_xticks(x_pos + bar_width / 2)
ax1.set_xticklabels(fruits_sorted, fontsize=12, rotation=45, ha='right')

plt.tight_layout()
plt.show()