import matplotlib.pyplot as plt
import numpy as np

disciplines = ['Quantum Physics', 'Genetics', 'Artificial Intelligence', 'Climate Science']
funding_percentages = [25, 20, 35, 20]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

fig, ax = plt.subplots(figsize=(12, 7))

# Plotting a horizontal bar chart with a different line style and marker
bars = ax.barh(disciplines, funding_percentages, color=colors, edgecolor='darkgrey', linestyle='--')

# Adding labels
ax.bar_label(bars, labels=[f'{p}%' for p in funding_percentages], label_type='edge', padding=3, color='purple')

# Set labels and title with new font properties
ax.set_xlabel('Percentage of Total Funding (%)', fontsize=13, fontfamily='serif', fontweight='bold')
ax.set_title('Research Funding Distribution Across Key Scientific Disciplines\nNIFR Annual Report',
             fontsize=16, fontweight='bold', color='darkred')

# Customize the x-axis
ax.set_xlim(0, 50)

# Adding a grid with altered appearance
ax.xaxis.grid(True, linestyle=':', linewidth=0.5, color='black')

descriptions = [
    "Exploring the quantum realm",
    "Decoding the blueprint of life",
    "Innovating intelligent solutions",
    "Combating climate change"
]

for bar, desc in zip(bars, descriptions):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, desc,
            va='center', ha='left', fontsize=10, color='darkblue')

# Adding a legend to describe the bars
ax.legend(['Funding %'], loc='lower right', frameon=False)

plt.tight_layout()
plt.show()