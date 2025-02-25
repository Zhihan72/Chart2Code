import matplotlib.pyplot as plt
import numpy as np

diets = ['Veg', 'Vgn', 'Pleo', 'Med', 'SW']
cholesterol_levels = {
    'Veg': [192, 182, 180, 184, 195, 190, 178, 188, 185, 190, 186, 185],
    'Vgn': [167, 165, 168, 160, 170, 155, 164, 162, 160, 158, 165, 170],
    'Pleo': [217, 215, 209, 202, 210, 198, 220, 213, 205, 200, 215, 207],
    'Med': [188, 190, 195, 192, 195, 193, 190, 187, 189, 185, 192, 200],
    'SW': [245, 240, 239, 250, 242, 230, 245, 238, 247, 240, 235, 248]
}

data = [np.array(cholesterol_levels[diet]) for diet in diets]

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Vertical box plot
bplot1 = axes[0].boxplot(data, vert=True, patch_artist=True, labels=diets, notch=True, whis=1.5)

colors = ['#FFCC33', '#33CC99', '#FF6633', '#3399FF', '#CC3333']
for patch, color in zip(bplot1['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

for whisker in bplot1['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle='--')

for cap in bplot1['caps']:
    cap.set(color='gray', linewidth=1.5)

for median in bplot1['medians']:
    median.set(color='black', linewidth=2)

for flier in bplot1['fliers']:
    flier.set(marker='o', color='#FF33CC', alpha=0.5)

axes[0].set_title('Cholesterol by Diet', fontsize=14, fontweight='bold', pad=20)
axes[0].set_xlabel('Diet', fontsize=12)
axes[0].set_ylabel('Cholesterol (mg/dL)', fontsize=12)
axes[0].grid(True, linestyle='--', which='both', alpha=0.7)

mean_cholesterol = [np.mean(levels) for levels in data]

# Line plot for mean levels
axes[1].plot(diets, mean_cholesterol, marker='o', color='b', linestyle='-', linewidth=2, markersize=10)
axes[1].set_title('Mean Levels', fontsize=14, fontweight='bold', pad=20)
axes[1].set_xlabel('Diet', fontsize=12)
axes[1].set_ylabel('Mean (mg/dL)', fontsize=12)
axes[1].set_ylim(160, 260)

for i, mean_val in enumerate(mean_cholesterol):
    axes[1].annotate(f'{mean_val:.1f}', (diets[i], mean_val),
                     textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10)

plt.tight_layout()
plt.show()