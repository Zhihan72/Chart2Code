import matplotlib.pyplot as plt
import numpy as np

diets = ['K', 'P', 'V', 'M', 'IF', 'C']

keto_weight_loss = [3.2, 3.1, 2.8, 2.9, 3.4, 3.3, 3.2, 2.9, 3.1, 3.0, 2.8, 3.1, 3.3, 3.0, 2.9, 3.0]
paleo_weight_loss = [3.0, 2.8, 3.2, 3.1, 2.9, 2.8, 3.0, 2.9, 3.1, 2.7, 2.8, 3.0, 2.9, 3.1, 3.0, 2.8]
vegan_weight_loss = [2.5, 2.4, 2.7, 2.8, 2.6, 2.4, 2.5, 2.6, 2.5, 2.3, 2.2, 2.4, 2.6, 2.5, 2.7, 2.8]
mediterranean_weight_loss = [2.8, 2.9, 3.0, 2.7, 2.8, 3.1, 3.0, 2.9, 2.8, 3.0, 2.9, 2.7, 3.1, 2.9, 3.0, 2.8]
intermittent_fasting_weight_loss = [3.5, 3.7, 3.6, 3.9, 3.8, 3.7, 3.6, 3.5, 3.7, 3.9, 3.8, 3.7, 3.5, 3.6, 3.7, 3.8]

# Adding Carnivore diet data
carnivore_weight_loss = [3.1, 3.3, 3.2, 3.1, 3.0, 3.2, 3.1, 3.0, 3.2, 3.1, 3.2, 3.3, 3.1, 3.4, 3.2, 3.0]

weight_loss_data = [
    keto_weight_loss, paleo_weight_loss,
    vegan_weight_loss, mediterranean_weight_loss,
    intermittent_fasting_weight_loss, carnivore_weight_loss
]

fig, ax = plt.subplots(figsize=(14, 10))

single_color = 'blue'

bp = ax.boxplot(weight_loss_data, vert=True, notch=True, patch_artist=True,
                labels=diets, 
                boxprops=dict(facecolor=single_color, color=single_color, alpha=0.7),
                whiskerprops=dict(color=single_color),
                capprops=dict(color=single_color),
                medianprops=dict(color=single_color, linewidth=2),
                flierprops=dict(marker='o', color=single_color, markersize=6, alpha=0.5))

means = [np.mean(data) for data in weight_loss_data]
ax.scatter(range(1, len(means) + 1), means, color=single_color, zorder=3)

ax.set_title('Weight Loss Over Diets', fontsize=16, fontweight='bold')
ax.set_ylabel('Loss (kg)', fontsize=14)
ax.set_xlabel('Diets', fontsize=14)

for spine in ax.spines.values():
    spine.set_visible(False)

plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()