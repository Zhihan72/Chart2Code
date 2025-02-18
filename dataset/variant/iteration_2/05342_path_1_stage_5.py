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
bars = ax.barh(hobbies, percentages, color='lightcoral', edgecolor='darkred', linewidth=1.5)
ax.bar_label(bars, fmt='%.0f%%', padding=3, fontsize=9)

ax.set_title("Quarantine Hobbies 2023", fontsize=20, fontweight='heavy', pad=15)
ax.set_xlabel("% of People", fontsize=14, fontweight='medium')
ax.set_xlim(0, 50)

ax.set_yticks(range(len(hobbies)))
ax.set_yticklabels(hobbies, rotation=0, fontsize=11)

ax.xaxis.grid(True, linestyle='-.', color='purple', alpha=0.6)

annotations = [
    ("Most Popular", 45),
    ("High Surge", 35),
    ("Major Outlet", 40)
]

for annotation, value in annotations:
    index = percentages.index(value)
    ax.annotate(annotation, xy=(value, index), 
                xytext=(value + 7, index),
                arrowprops=dict(arrowstyle="-|>", color='blue'),
                fontsize=11, color='blue')

plt.legend(["Highlighted Activities"], loc='lower right', fontsize=10)

plt.gca().spines['top'].set_linewidth(1.5)
plt.gca().spines['right'].set_linewidth(1.5)

plt.tight_layout()
plt.show()