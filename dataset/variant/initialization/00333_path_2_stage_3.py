import matplotlib.pyplot as plt
import numpy as np

disciplines = ['Quantum Physics', 'Genetics', 'Artificial Intelligence', 
               'Climate Science', 'Neuroscience', 'Robotics']
funding_percentages = [25, 20, 35, 20, 15, 25]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Sort the data by funding percentages in descending order
sorted_indices = np.argsort(funding_percentages)[::-1]
disciplines = [disciplines[i] for i in sorted_indices]
funding_percentages = [funding_percentages[i] for i in sorted_indices]
colors = [colors[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(disciplines, funding_percentages, color=colors, edgecolor='darkgrey', linestyle='--')

ax.bar_label(bars, labels=[f'{p}%' for p in funding_percentages], label_type='edge', padding=3, color='purple')

ax.set_xlabel('Percentage of Total Funding (%)', fontsize=13, fontfamily='serif', fontweight='bold')
ax.set_title('Research Funding Distribution Across Key Scientific Disciplines\nNIFR Annual Report',
             fontsize=16, fontweight='bold', color='darkred')

ax.set_xlim(0, 50)
ax.xaxis.grid(True, linestyle=':', linewidth=0.5, color='black')

descriptions = [
    "Exploring the quantum realm",
    "Decoding the blueprint of life",
    "Innovating intelligent solutions",
    "Combating climate change",
    "Unlocking the mysteries of the brain",
    "Developing the robots of tomorrow"
]
descriptions = [descriptions[i] for i in sorted_indices]

for bar, desc in zip(bars, descriptions):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, desc,
            va='center', ha='left', fontsize=10, color='darkblue')

ax.legend(['Funding %'], loc='lower right', frameon=False)

plt.tight_layout()
plt.show()