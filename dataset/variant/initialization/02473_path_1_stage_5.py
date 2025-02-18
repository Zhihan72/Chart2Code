import matplotlib.pyplot as plt
import numpy as np

regions = ["Transylv.", "Loch Ness", "Himalayas", "Amazon", 
           "Aust. Outback", "Pac. NW"]

cryptid_counts = [15, 8, 12, 10, 7, 20]

uniform_color = '#8B4513'

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(regions, cryptid_counts, color=uniform_color)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
            f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

ax.set_ylim(0, max(cryptid_counts) + 5)

plt.show()