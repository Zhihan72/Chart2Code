import matplotlib.pyplot as plt
import numpy as np

# Categories and percentages of people picking up hobbies during quarantine
hobbies = [
    "Cooking", 
    "Reading", 
    "Gardening", 
    "DIY", 
    "Exercise", 
    "Gaming", 
    "Music", 
    "Crafting", 
    "Photo", 
    "Writing"
]

percentages = [35, 30, 25, 20, 45, 40, 15, 10, 5, 8]
colors = plt.cm.Paired(np.linspace(0, 1, len(hobbies)))

# Bar chart
fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(hobbies, percentages, color=colors, edgecolor='black')
ax.bar_label(bars, fmt='%.0f%%', padding=5, fontsize=10)

# Simplified title and labels
ax.set_title("Quarantine Hobbies 2023", fontsize=18, fontweight='bold', pad=15)
ax.set_ylabel("% of People", fontsize=14)
ax.set_ylim(0, 50)
ax.set_xticklabels(hobbies, rotation=45, ha='right', fontsize=12)

ax.set_xticks(range(len(hobbies)))
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Highlight top 3 hobbies
annotations = [
    ("Most Popular", 45),
    ("High Surge", 35),
    ("Major Outlet", 40)
]

for annotation, value in annotations:
    hobby_index = percentages.index(value)
    ax.annotate(annotation, xy=(hobby_index, value), 
                xytext=(hobby_index, value + 5),
                arrowprops=dict(arrowstyle="->", color='black'),
                fontsize=10, color='black')

plt.tight_layout()
plt.show()