import matplotlib.pyplot as plt
import numpy as np

proteins = [3.1, 3.5, 2.8, 3.0, 3.2, 3.6, 3.4, 2.9, 3.3, 3.1]
carbohydrates = [4.5, 4.3, 4.9, 4.6, 4.4, 4.7, 4.2, 4.8, 4.1, 4.5]
fats = [0.5, 0.8, 0.6, 0.4, 0.7, 0.6, 0.5, 0.9, 0.8, 0.6]
fibers = [1.4, 1.5, 1.3, 1.6, 1.5, 1.4, 1.7, 1.3, 1.5, 1.6]
vitamins = [0.9, 1.1, 1.0, 0.8, 1.1, 1.2, 1.0, 0.9, 1.3, 1.1]
minerals = [0.5, 0.7, 0.6, 0.8, 0.5, 0.6, 0.7, 0.4, 0.7, 0.6]  # New data series

data = [proteins, carbohydrates, fats, fibers, vitamins, minerals]
nutrient_labels = ['Fats', 'Carbohydrates', 'Vitamins', 'Fibers', 'Proteins', 'Minerals']

fig, ax = plt.subplots(figsize=(12, 8))

violin_parts = ax.violinplot(data, vert=False, showmeans=True, showmedians=True)
colors = ['lightgrey', 'lightgreen', 'lightyellow', 'lightpink', 'lightblue', 'lightcoral']  # Added color
edge_colors = ['darkslategray', 'darkgreen', 'gold', 'crimson', 'navy', 'brown']             # Added edge color

for i, pc in enumerate(violin_parts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor(edge_colors[i])
    pc.set_alpha(0.5 + i * 0.1)

for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians', 'cmeans'):
    vp = violin_parts[partname]
    vp.set_edgecolor('black')
    vp.set_linewidth(2)

medians = [np.median(nutrient) for nutrient in data]
for i, median in enumerate(medians):
    plt.text(median, i + 1, f'{median:.2f}', verticalalignment='center', size=10, color='brown')

ax.set_title('Nutritional Composition of Mushrooms', fontsize=18, weight='bold')
ax.set_xlabel('Quantity (g/100g)', fontsize=14, style='italic')
ax.set_ylabel('Nutrient Category', fontsize=14, style='italic')
ax.set_yticks(range(1, len(data) + 1))
ax.set_yticklabels(nutrient_labels, fontsize=12)

ax.xaxis.grid(True, linestyle=':', linewidth=1, which='both', color='purple', alpha=0.3)

plt.tight_layout()

plt.show()