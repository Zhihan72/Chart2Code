import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
happiness_data = [
    [7, 8, 7, 6, 8, 8, 7, 9, 7, 6, 7, 8, 7, 8, 7],  
    [6, 7, 6, 6, 7, 7, 6, 6, 6, 7, 6, 6, 5, 6, 6],  
    [5, 6, 5, 6, 6, 5, 6, 6, 5, 5, 5, 5, 5, 6, 5],  
    [6, 6, 5, 4, 5, 6, 5, 4, 4, 5, 6, 5, 4, 5, 5],  
    [7, 6, 7, 6, 7, 7, 7, 6, 6, 7, 8, 7, 8, 7, 7]   
]

fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(happiness_data, vert=True, patch_artist=True, labels=age_groups, notch=True, meanline=True, showmeans=True)

colors = ['#FF6347', '#FFD700', '#ADFF2F', '#1E90FF', '#DA70D6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['means'], color='blue')
plt.setp(box['medians'], color='red')

medians = [np.median(group) for group in happiness_data]
ax.plot(range(1, len(age_groups) + 1), medians, color='purple', marker='D', linestyle='-.', label='Median Score')

ax.set_title('Happiness by Age', fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Score', fontsize=12)
ax.set_xlabel('Age', fontsize=12)

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)
ax.set_facecolor('#f0f0f0')

ax.legend()

for i, age_group in enumerate(age_groups):
    ax.text(i + 1, max(happiness_data[i]) + 0.5, f'Max: {max(happiness_data[i])}', 
            ha='center', fontsize=10, color=colors[i])

plt.tight_layout()
plt.show()