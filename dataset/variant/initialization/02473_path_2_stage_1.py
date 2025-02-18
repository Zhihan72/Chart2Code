import matplotlib.pyplot as plt
import numpy as np

regions = ["Loch Ness", "Pacific Northwest", "Himalayas", "Amazon Rainforest",
           "Bermuda Triangle", "Australian Outback", "Transylvania"]
cryptid_counts = [8, 20, 12, 10, 5, 7, 15]

colors = ['#1E90FF', '#DAA520', '#228B22', '#32CD32', '#9400D3', '#FFD700', '#8B4513']

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(regions, cryptid_counts, color=colors, edgecolor='black', height=0.6)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{int(width)}', ha='center', va='center', fontsize=10, color='black')

ax.set_xlabel('Number of Mysterious Creatures', fontsize=12, fontweight='bold')
ax.set_title('Mythical Creature Analysis:\nLeading Regions Known for Legends', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlim(0, max(cryptid_counts) + 5)
ax.grid(axis='x', linestyle='--', alpha=0.7)

ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions, fontsize=11, weight='bold')

plt.tight_layout()

plt.show()