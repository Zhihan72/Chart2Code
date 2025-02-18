import matplotlib.pyplot as plt
import numpy as np

regions = ["Transylv.", "Loch Ness", "Himalayas", "Amazon", 
           "Aust. Outback", "Pac. NW", "Bermuda"]

cryptid_counts = [15, 8, 12, 10, 7, 20, 5]

# Apply a single color consistently across all data groups
uniform_color = '#8B4513'  # Use the first color from the original list

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.barh(regions, cryptid_counts, color=uniform_color, edgecolor='black', height=0.6)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{int(width)}', ha='center', va='center', fontsize=10, color='black')

ax.set_xlabel('Unique Species Count', fontsize=12, fontweight='bold')
ax.set_title('Mythical Creatures by Region', fontsize=16, fontweight='bold', pad=20)
ax.set_xlim(0, max(cryptid_counts) + 5)
ax.grid(axis='x', linestyle='--', alpha=0.7)

ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions, fontsize=11, weight='bold')

plt.tight_layout()
plt.show()