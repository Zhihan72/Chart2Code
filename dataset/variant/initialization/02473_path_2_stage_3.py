import matplotlib.pyplot as plt
import numpy as np

regions = ["Loch Ness", "Pacific Northwest", "Himalayas", "Amazon Rainforest",
           "Bermuda Triangle", "Australian Outback", "Transylvania"]
cryptid_counts = [8, 20, 12, 10, 5, 7, 15]

# Manually shuffled colors
colors = ['#FFD700', '#9400D3', '#8B4513', '#32CD32', '#DAA520', '#228B22', '#1E90FF']

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(regions, cryptid_counts, color=colors, edgecolor='black', width=0.6)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
            f'{int(height)}', ha='center', va='center', fontsize=10, color='black')

ax.set_ylabel('Number of Mysterious Creatures', fontsize=12, fontweight='bold')
ax.set_title('Mythical Creature Analysis:\nLeading Regions Known for Legends', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylim(0, max(cryptid_counts) + 5)
ax.grid(axis='y', linestyle='--', alpha=0.7)

ax.set_xticklabels(regions, fontsize=11, weight='bold')

plt.tight_layout()

plt.show()