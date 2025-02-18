import matplotlib.pyplot as plt
import numpy as np

regions = ["Transylv.", "Loch Ness", "Himalayas", "Amazon", 
           "Aust. Outback", "Pac. NW", "Bermuda"]

cryptid_counts = [15, 8, 12, 10, 7, 20, 5]

uniform_color = '#8B4513'  

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(regions, cryptid_counts, color=uniform_color, edgecolor='black')

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
            f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

ax.set_ylabel('Unique Species Count', fontsize=12, fontweight='bold')
ax.set_title('Mythical Creatures by Region', fontsize=16, fontweight='bold', pad=20)
ax.set_ylim(0, max(cryptid_counts) + 5)
ax.grid(axis='y', linestyle='--', alpha=0.7)

ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, fontsize=11, weight='bold')

plt.tight_layout()
plt.show()