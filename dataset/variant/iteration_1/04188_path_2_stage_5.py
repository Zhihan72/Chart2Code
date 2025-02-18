import matplotlib.pyplot as plt
import numpy as np

# Nutrient concentrations for mushrooms
proteins = [3.1, 3.5, 2.8, 3.0, 3.2, 3.6, 3.4, 2.9, 3.3, 3.1]
carbs = [4.5, 4.3, 4.9, 4.6, 4.4, 4.7, 4.2, 4.8, 4.1, 4.5]
vitamins = [0.9, 1.1, 1.0, 0.8, 1.1, 1.2, 1.0, 0.9, 1.3, 1.1]

data = [proteins, carbs, vitamins]
nutrient_labels = ['Prot', 'Carbs', 'Vits']

fig, ax = plt.subplots(figsize=(10, 8))

violin_parts = ax.violinplot(data, vert=False, showmeans=True, showmedians=True)

colors = ['lightcoral', 'royalblue', 'plum']

for idx, pc in enumerate(violin_parts['bodies']):
    pc.set_facecolor(colors[idx])
    pc.set_edgecolor(colors[(idx + 1) % len(colors)])
    pc.set_alpha(0.7)

for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians', 'cmeans'):
    vp = violin_parts[partname]
    vp.set_edgecolor('darkgreen')
    vp.set_linewidth(1.5)

# Annotate median values
medians = [np.median(nutrient) for nutrient in data]
for i, median in enumerate(medians):
    plt.text(median, i + 1, f'{median:.2f}', verticalalignment='center', size=12, color='red')

ax.set_yticks(range(1, len(data) + 1))
ax.set_yticklabels(nutrient_labels, fontsize=12)

plt.tight_layout()
plt.show()