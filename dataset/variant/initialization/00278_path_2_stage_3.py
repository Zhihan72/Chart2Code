import matplotlib.pyplot as plt
import numpy as np

wonders = [
    "Pyramid of Giza", "Gardens of Babylon",
    "Zeus at Olympia", "Temple of Artemis",
    "Mausoleum Halicarnassus", "Colossus of Rhodes", 
    "Lighthouse Alexandria"
]

tourists = np.array([450, 380, 270, 310, 200, 290, 410])

new_colors = ['#ff7f0e', '#9467bd', '#2ca02c', '#8c564b', '#1f77b4', '#d62728', '#e377c2']

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(wonders, tourists, color=new_colors, linewidth=1.5, edgecolor='grey', linestyle='-.')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval}k', ha='center', va='bottom', fontsize=10, color='darkblue')

ax.set_title('Attraction in 100 AD:\n7 Ancient Wonders', fontsize=16, pad=20, style='italic')
ax.set_xlabel('Ancient World Wonders', fontsize=12)
ax.set_ylabel('Tourists (thousands)', fontsize=12)

plt.xticks(rotation=45, ha='right')

ax.yaxis.grid(True, linestyle=':', alpha=0.4)
ax.xaxis.grid(True, which='minor', linestyle='--', alpha=0.2)
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))

ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['top'].set_color('black')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

plt.tight_layout()
plt.show()