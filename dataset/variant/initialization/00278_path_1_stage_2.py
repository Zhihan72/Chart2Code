import matplotlib.pyplot as plt
import numpy as np

wonders = [
    "Pyramid of Giza", "Gardens of Babylon",
    "Zeus Statue", "Artemis Temple",
    "Mausoleum", "Colossus", "Lighthouse"
]

tourists = np.array([450, 380, 270, 310, 200, 290, 410])

colors = ['#FF3366', '#FF6600', '#CCFF33', '#FF33CC', '#00CCFF', '#66FF33', '#FFCC00']

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(wonders, tourists, color=colors, edgecolor='darkgrey', hatch='/')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval}k', ha='center', va='bottom', fontsize=10, color='navy')

ax.set_title('Tourists in 100 AD: Ancient Wonders', fontsize=18, pad=30)
ax.set_xlabel('Ancient Wonders', fontsize=14, style='italic')
ax.set_ylabel('Tourists (thousands)', fontsize=14, style='italic')

plt.xticks(rotation=30, ha='right')

ax.yaxis.grid(True, linestyle='-.', linewidth=0.5)

plt.tight_layout()

plt.show()