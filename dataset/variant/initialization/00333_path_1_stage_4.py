import matplotlib.pyplot as plt

# Data preparation
disciplines = ['Artificial Intelligence', 'Quantum Physics', 'Climate Science']
funding_percentages = [35, 25, 20]
new_colors = ['#4682b4', '#ff6347', '#8a2be2']
descriptions = [
    "Innovating intelligent solutions",
    "Exploring the quantum realm",
    "Combating climate change"
]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.barh(disciplines, funding_percentages, color=new_colors, edgecolor='brown', linestyle='dashed', hatch='o')
ax.bar_label(bars, labels=[f'{p}%' for p in funding_percentages], label_type='edge', padding=3)
ax.set_xlabel('Percentage of Total Funding (%)', fontsize=12)
ax.set_title('Research Funding Distribution Across Key Scientific Disciplines\nNIFR Annual Report',
             fontsize=14, fontweight='bold')
ax.set_xlim(0, 50)

for bar, desc in zip(bars, descriptions):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, desc,
            va='center', ha='left', fontsize=10, color='grey')

# Random alterations in stylistic elements
ax.legend(['AI', 'QP', 'CS'], loc='lower right', fontsize=10, frameon=False)
ax.grid(True, which='both', axis='x', color='grey', linestyle='--', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#cd5c5c')
ax.spines['left'].set_color('#cd5c5c')

plt.tight_layout()
plt.show()