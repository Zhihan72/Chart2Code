import matplotlib.pyplot as plt
import numpy as np

diets = ['Veg', 'Vgn', 'Pal', 'Med', 'West', 'Keto', 'Low-Carb']
cholesterol_levels = {
    'Vegetarian': [180, 190, 185, 195, 178, 182, 188, 185, 192, 190, 186, 184],
    'Vegan': [170, 160, 165, 155, 168, 162, 158, 164, 170, 165, 160, 167],
    'Paleo': [220, 215, 210, 205, 198, 200, 202, 207, 215, 213, 209, 217],
    'Mediterranean': [195, 190, 192, 185, 187, 189, 192, 195, 200, 188, 190, 193],
    'Standard Western': [230, 240, 235, 245, 238, 242, 239, 247, 250, 245, 248, 240],
    'Keto': [200, 205, 198, 210, 207, 202, 200, 208, 215, 210, 212, 213],
    'Low-Carb': [210, 215, 205, 202, 210, 208, 206, 215, 210, 212, 214, 210]
}

data = [np.array(cholesterol_levels[diet]) for diet in cholesterol_levels.keys()]

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

bplot1 = axes[0].boxplot(data, vert=False, patch_artist=True, labels=diets, notch=True, whis=1.5)

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF99CC', '#FFD700', '#8A2BE2']
for patch, color in zip(bplot1['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

for whisker in bplot1['whiskers']:
    whisker.set(color='blue', linewidth=2, linestyle='-.')

for cap in bplot1['caps']:
    cap.set(color='purple', linewidth=2)

for median in bplot1['medians']:
    median.set(color='yellow', linewidth=3)

for flier in bplot1['fliers']:
    flier.set(marker='s', color='green', alpha=0.7)

axes[0].set_title('Cholesterol by Diet', fontsize=14, fontweight='bold', pad=15)
axes[0].set_xlabel('Cholesterol (mg/dL)', fontsize=12)
axes[0].set_ylabel('Diet', fontsize=12)
axes[0].grid(True, linestyle='-', which='major', alpha=0.5)

mean_cholesterol = [np.mean(levels) for levels in data]

axes[1].plot(diets, mean_cholesterol, marker='x', color='c', linestyle='--', linewidth=1.5, markersize=12)
axes[1].set_title('Mean Cholesterol', fontsize=14, fontweight='bold', pad=15)
axes[1].set_xlabel('Diet', fontsize=12)
axes[1].set_ylabel('Mean Chol. (mg/dL)', fontsize=12)
axes[1].set_ylim(160, 260)
axes[1].yaxis.set_label_position("right")
axes[1].yaxis.tick_right()

for i, mean_val in enumerate(mean_cholesterol):
    axes[1].annotate(f'{mean_val:.1f}', (diets[i], mean_val),
                     textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

plt.tight_layout()
plt.show()