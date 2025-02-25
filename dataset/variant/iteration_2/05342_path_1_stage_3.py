import matplotlib.pyplot as plt
import numpy as np

hobbies = [
    "DIY", 
    "Music", 
    "Cooking", 
    "Writing", 
    "Gardening", 
    "Photo", 
    "Gaming", 
    "Exercise", 
    "Crafting", 
    "Reading"
]

percentages = [20, 40, 35, 8, 25, 5, 15, 45, 10, 30]

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(hobbies, percentages, color='skyblue', edgecolor='black')
ax.bar_label(bars, fmt='%.0f%%', padding=5, fontsize=10)

ax.set_title("Quarantine Hobbies 2023", fontsize=18, fontweight='bold', pad=15)
ax.set_ylabel("% of People", fontsize=14)
ax.set_ylim(0, 50)
ax.set_xticklabels(hobbies, rotation=45, ha='right', fontsize=12)

ax.set_xticks(range(len(hobbies)))
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

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