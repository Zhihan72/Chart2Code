import matplotlib.pyplot as plt
import numpy as np

# Nutrient concentrations for mushrooms
proteins = [3.1, 3.5, 2.8, 3.0, 3.2, 3.6, 3.4, 2.9, 3.3, 3.1]
carbs = [4.5, 4.3, 4.9, 4.6, 4.4, 4.7, 4.2, 4.8, 4.1, 4.5]
fats = [0.5, 0.8, 0.6, 0.4, 0.7, 0.6, 0.5, 0.9, 0.8, 0.6]
fibers = [1.4, 1.5, 1.3, 1.6, 1.5, 1.4, 1.7, 1.3, 1.5, 1.6]
vitamins = [0.9, 1.1, 1.0, 0.8, 1.1, 1.2, 1.0, 0.9, 1.3, 1.1]

data = [proteins, carbs, fats, fibers, vitamins]
nutrient_labels = ['Prot', 'Carbs', 'Fats', 'Fibers', 'Vits']

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 8))

# Create horizontal violin plot
violin_parts = ax.violinplot(data, vert=False, showmeans=True, showmedians=True)

# Manually shuffled colors for each part
colors = ['lightcoral', 'royalblue', 'gold', 'mediumseagreen', 'plum']

for idx, pc in enumerate(violin_parts['bodies']):
    pc.set_facecolor(colors[idx])
    pc.set_edgecolor(colors[(idx + 1) % len(colors)])  # Use the next color for edge
    pc.set_alpha(0.7)

for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians', 'cmeans'):
    vp = violin_parts[partname]
    vp.set_edgecolor('darkgreen')
    vp.set_linewidth(1.5)

# Annotate median values
medians = [np.median(nutrient) for nutrient in data]
for i, median in enumerate(medians):
    plt.text(median, i + 1, f'{median:.2f}', verticalalignment='center', size=12, color='red')

# Customize the plot
ax.set_title('Mushroom Nutrients', fontsize=16, weight='bold')
ax.set_ylabel('Type', fontsize=14)
ax.set_xlabel('Concentration (g/100g)', fontsize=14)
ax.set_yticks(range(1, len(data) + 1))
ax.set_yticklabels(nutrient_labels, fontsize=12)
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()