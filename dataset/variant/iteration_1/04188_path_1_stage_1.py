import matplotlib.pyplot as plt
import numpy as np

proteins = [3.1, 3.5, 2.8, 3.0, 3.2, 3.6, 3.4, 2.9, 3.3, 3.1]
carbohydrates = [4.5, 4.3, 4.9, 4.6, 4.4, 4.7, 4.2, 4.8, 4.1, 4.5]
fats = [0.5, 0.8, 0.6, 0.4, 0.7, 0.6, 0.5, 0.9, 0.8, 0.6]
fibers = [1.4, 1.5, 1.3, 1.6, 1.5, 1.4, 1.7, 1.3, 1.5, 1.6]
vitamins = [0.9, 1.1, 1.0, 0.8, 1.1, 1.2, 1.0, 0.9, 1.3, 1.1]

data = [proteins, carbohydrates, fats, fibers, vitamins]
nutrient_labels = ['Vitamins', 'Proteins', 'Fibers', 'Carbohydrates', 'Fats']  # Shuffled labels

fig, ax = plt.subplots(figsize=(14, 8))

violin_parts = ax.violinplot(data, showmeans=True, showmedians=True)
for pc in violin_parts['bodies']:
    pc.set_facecolor('aquamarine')
    pc.set_edgecolor('mediumseagreen')
    pc.set_alpha(0.7)
for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians', 'cmeans'):
    vp = violin_parts[partname]
    vp.set_edgecolor('darkgreen')
    vp.set_linewidth(1.5)

medians = [np.median(nutrient) for nutrient in data]
for i, median in enumerate(medians):
    plt.text(i + 1, median, f'{median:.2f}', horizontalalignment='center', size=12, color='red')

ax.set_title('Variability in Mushroom Nutrition', fontsize=16, weight='bold')  # Altered title
ax.set_xlabel('Type of Nutrient', fontsize=14)  # Altered x-axis label
ax.set_ylabel('Content (g/100g)', fontsize=14)  # Altered y-axis label
ax.set_xticks(range(1, len(data) + 1))
ax.set_xticklabels(nutrient_labels, fontsize=12)  # Shuffled group labels
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.tight_layout()

plt.show()