import matplotlib.pyplot as plt

# Data preparation
disciplines = ['Quantum Physics', 'Artificial Intelligence', 'Climate Science']
funding_percentages = [25, 35, 20]
new_colors = ['#ff6347', '#4682b4', '#8a2be2']
descriptions = [
    "Exploring the quantum realm",
    "Innovating intelligent solutions",
    "Combating climate change"
]

# Sort the data in descending order
sorted_indices = sorted(range(len(funding_percentages)), key=lambda i: funding_percentages[i], reverse=True)
disciplines = [disciplines[i] for i in sorted_indices]
funding_percentages = [funding_percentages[i] for i in sorted_indices]
new_colors = [new_colors[i] for i in sorted_indices]
descriptions = [descriptions[i] for i in sorted_indices]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.barh(disciplines, funding_percentages, color=new_colors, edgecolor='black')
ax.bar_label(bars, labels=[f'{p}%' for p in funding_percentages], label_type='edge', padding=3)
ax.set_xlabel('Percentage of Total Funding (%)', fontsize=12)
ax.set_title('Research Funding Distribution Across Key Scientific Disciplines\nNIFR Annual Report',
             fontsize=14, fontweight='bold')
ax.set_xlim(0, 50)

# Annotate each discipline with a brief description
for bar, desc in zip(bars, descriptions):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, desc,
            va='center', ha='left', fontsize=10, color='grey')

plt.tight_layout()
plt.show()