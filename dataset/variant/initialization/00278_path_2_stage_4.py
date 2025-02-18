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
bars = ax.barh(wonders, tourists, color=new_colors, linewidth=1.5, edgecolor='grey', linestyle='-.')

for bar in bars:
    xval = bar.get_width()
    ax.text(xval + 10, bar.get_y() + bar.get_height() / 2, f'{xval}k', va='center', ha='left', fontsize=10, color='darkblue')

ax.set_title('Attraction in 100 AD:\n7 Ancient Wonders', fontsize=16, pad=20, style='italic')
ax.set_xlabel('Tourists (thousands)', fontsize=12)
ax.set_ylabel('Ancient World Wonders', fontsize=12)

plt.yticks(rotation=0)

ax.xaxis.grid(True, linestyle=':', alpha=0.4)
ax.yaxis.grid(True, which='minor', linestyle='--', alpha=0.2)
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))

ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['top'].set_color('black')
ax.spines['bottom'].set_linewidth(1.2)
ax.spines['left'].set_linewidth(1.2)

plt.tight_layout()
plt.show()