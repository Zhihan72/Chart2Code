import matplotlib.pyplot as plt
import numpy as np

regions = ["Loch Ness", "Pacific Northwest", "Himalayas", "Amazon Rainforest",
           "Bermuda Triangle", "Australian Outback", "Transylvania"]

cryptid_counts = [10, 8, 15, 7, 12, 5, 20]

colors = ['#DAA520', '#FFD700', '#1E90FF', '#8B4513', '#32CD32', '#9400D3', '#228B22']

fig, ax = plt.subplots(figsize=(12, 7))

ax.bar(regions, cryptid_counts, color=colors, edgecolor='black', width=0.6)

ax.set_ylim(0, max(cryptid_counts) + 5)

plt.tight_layout()
plt.show()