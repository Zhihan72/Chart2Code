import matplotlib.pyplot as plt
import numpy as np

disciplines = ['Quantum Physics', 'Genetics', 'Artificial Intelligence', 
               'Climate Science', 'Neuroscience', 'Robotics']
funding_percentages = [25, 20, 35, 20, 15, 25]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

sorted_indices = np.argsort(funding_percentages)[::-1]
disciplines = [disciplines[i] for i in sorted_indices]
funding_percentages = [funding_percentages[i] for i in sorted_indices]
colors = [colors[i] for i in sorted_indices]

shuffled_colors = [colors[1], colors[4], colors[0], colors[5], colors[2], colors[3]]

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(disciplines, funding_percentages, color=shuffled_colors, edgecolor='darkgrey', linestyle='--')

ax.bar_label(bars, labels=[f'{p}%' for p in funding_percentages], label_type='edge', padding=3, color='purple')

titles = [
    'Analyzing Funding Distribution in Scientific Disciplines\n2023 NIFR Survey Results',
    'Key Scientific Fields Funding Overview\nData from the Latest Report',
    'Funding Sources Within Science Research Fields\nAnnual Analysis Report'
]
axis_labels = [
    'Funding Allocation (%)',
    'Distribution of Resources (%)',
    'Percentage of Science Funding (%)'
]
ax.set_title(titles[1], fontsize=16, fontweight='bold', color='darkred')
ax.set_xlabel(axis_labels[0], fontsize=13, fontfamily='serif', fontweight='bold')

ax.set_xlim(0, 50)
ax.xaxis.grid(True, linestyle=':', linewidth=0.5, color='black')

descriptions = [
    "Exploring the quantum realm",
    "Innovating intelligent solutions",
    "Unlocking the mysteries of the brain",
    "Developing the robots of tomorrow",
    "Decoding the blueprint of life",
    "Combating climate change"
]
descriptions = [descriptions[i] for i in sorted_indices]

for bar, desc in zip(bars, descriptions):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, desc,
            va='center', ha='left', fontsize=10, color='darkblue')

ax.legend(['Funding %'], loc='lower right', frameon=False)

plt.tight_layout()
plt.show()