import matplotlib.pyplot as plt
import numpy as np

# Regions remain the same as they define the original dimensional structure
regions = ["Loch Ness", "Pacific Northwest", "Himalayas", "Amazon Rainforest",
           "Bermuda Triangle", "Australian Outback", "Transylvania"]

# Cryptid counts are manually shuffled
cryptid_counts = [10, 8, 15, 7, 12, 5, 20]

# Colors are manually retained; they should align with the shuffled counts
colors = ['#DAA520', '#FFD700', '#1E90FF', '#8B4513', '#32CD32', '#9400D3', '#228B22']

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