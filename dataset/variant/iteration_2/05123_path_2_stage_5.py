import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
happiness_data = [
    [8, 6, 7, 9, 6, 7, 7, 8, 7, 6, 8, 7, 8, 7, 7],  
    [6, 7, 6, 5, 7, 6, 6, 7, 6, 6, 6, 7, 6, 6, 6],  
    [5, 5, 5, 6, 5, 6, 6, 6, 5, 5, 6, 5, 5, 5, 5],  
    [4, 4, 5, 5, 5, 6, 5, 6, 5, 4, 5, 4, 6, 5, 5],  
    [6, 7, 7, 7, 7, 6, 7, 6, 8, 7, 7, 6, 7, 8, 7]
]

fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(happiness_data, vert=False, patch_artist=True, labels=age_groups, notch=True, meanline=True, showmeans=True)

colors = ['#1E90FF', '#DA70D6', '#FF6347', '#ADFF2F', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['means'], color='blue')
plt.setp(box['medians'], color='red')

medians = [np.median(group) for group in happiness_data]
ax.plot(medians, range(1, len(age_groups) + 1), color='purple', marker='D', linestyle='-.')

ax.set_title('Happiness by Age', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Score', fontsize=12)
ax.set_ylabel('Age', fontsize=12)

plt.tight_layout()
plt.show()