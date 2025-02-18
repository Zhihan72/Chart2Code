import matplotlib.pyplot as plt
import numpy as np

age_labels = ['18-25', '26-35', '36-45', '46-60', '60+']

coffee_data = np.array([40, 35, 30, 25, 15])
tea_data = np.array([20, 25, 30, 35, 40])

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.6
positions = np.arange(len(age_labels))

coffee_offset = -coffee_data / 2
tea_offset = np.zeros_like(tea_data)

ax.bar(positions, -coffee_data, bar_width, bottom=coffee_offset, color='#1f77b4')  # Coffee: Blue
ax.bar(positions, tea_data, bar_width, bottom=tea_offset, color='#2ca02c')  # Tea: Green

for bars in ax.containers:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{abs(height)}%',
                    xy=(bar.get_x() + bar.get_width() / 2, (bar.get_y() + bar.get_y() + height) / 2),
                    xytext=(0, 0), 
                    textcoords='offset points',
                    ha='center', va='center', fontsize=10, color='black')

ax.set_xticks(positions)
ax.set_xticklabels(age_labels)

plt.axhline(y=0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()