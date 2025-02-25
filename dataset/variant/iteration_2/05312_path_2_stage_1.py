import matplotlib.pyplot as plt
import numpy as np

# Magical Creatures
creatures = ['Dragon', 'Elf', 'Troll', 'Fairy', 'Human']

# Scores for each creature
scores = {
    'Dragon': [95, 85, 90, 92, 85],
    'Elf': [70, 95, 80, 60, 90],
    'Troll': [80, 60, 75, 85, 50],
    'Fairy': [60, 85, 95, 70, 90],
    'Human': [75, 80, 70, 75, 85]
}

# Prepare box plot data
box_plot_data = [scores[creature] for creature in creatures]

# Plot setup
fig, ax = plt.subplots(figsize=(14, 8))

# Customizing the boxplot
boxprops = dict(linestyle='--', linewidth=1.5, color='purple', facecolor='lightyellow')
medianprops = dict(linestyle='-', linewidth=2, color='orange')
whiskerprops = dict(linestyle=':', linewidth=1.2, color='gray')
capprops = dict(linestyle='-.', linewidth=2, color='black')

# Create the vertical box plot
ax.boxplot(box_plot_data, labels=creatures, patch_artist=True,
           boxprops=boxprops, medianprops=medianprops,
           whiskerprops=whiskerprops, capprops=capprops,
           flierprops=dict(marker='^', color='red', markersize=7, alpha=0.7),
           notch=True)

# Add plot details
ax.set_title("Mystic World Survey: Attributes Score of Magical Creatures", fontsize=16, fontweight='bold', loc='left')
ax.set_ylabel('Attribute Score (0-100)', fontsize=12)
ax.set_xlabel('Magical Creatures', fontsize=12)
ax.grid(axis='y', linestyle='-.', alpha=0.5)

# Annotate observations
ax.annotate('Highest Vitality', xy=(1, scores['Dragon'][3]), xytext=(1.2, scores['Dragon'][3] + 5),
            arrowprops=dict(facecolor='black', arrowstyle='-|>'), fontsize=10, color='purple')
ax.annotate('Exceptional Charisma', xy=(2, scores['Elf'][4]), xytext=(2.2, scores['Elf'][4] + 5),
            arrowprops=dict(facecolor='black', arrowstyle='-|>'), fontsize=10, color='red')

# Automatically adjust the layout
plt.tight_layout()

# Show the chart
plt.show()