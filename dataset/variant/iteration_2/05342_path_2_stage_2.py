import matplotlib.pyplot as plt
import numpy as np

hobbies = [
    "Photography", 
    "Writing", 
    "Crafting", 
    "Music", 
    "Gardening", 
    "Reading", 
    "Cooking/Baking", 
    "Gaming", 
    "Exercise"
]

percentages = [5, 8, 10, 15, 25, 30, 35, 40, 45]

colors = plt.cm.Paired(np.linspace(0, 1, len(hobbies)))

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(hobbies, percentages, color=colors, edgecolor='black')
ax.bar_label(bars, fmt='%.0f%%', padding=5, fontsize=10)
ax.set_title("Popular Hobbies During Quarantine in 2023",
             fontsize=18, fontweight='bold', pad=15)
ax.set_ylabel("Percentage (%)", fontsize=14)
ax.set_ylim(0, 50)
ax.set_xticklabels(hobbies, rotation=45, ha='right', fontsize=12)
ax.set_xticks(range(len(hobbies)))
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
plt.tight_layout()
plt.show()