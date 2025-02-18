import matplotlib.pyplot as plt
import numpy as np

wonders = [
    "Great Pyramid of Giza", "Hanging Gardens of Babylon",
    "Statue of Zeus at Olympia", "Temple of Artemis at Ephesus",
    "Mausoleum at Halicarnassus", "Colossus of Rhodes", 
    "Lighthouse of Alexandria"
]

tourists = np.array([450, 380, 270, 310, 200, 290, 410])

# Change the color palette
new_colors = ['#ff7f0e', '#9467bd', '#2ca02c', '#8c564b', '#1f77b4', '#d62728', '#e377c2']

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(wonders, tourists, color=new_colors, linewidth=1.5, edgecolor='grey', linestyle='-.')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval}k', ha='center', va='bottom', fontsize=10, color='darkblue')

ax.set_title('Tourist Attraction in 100 AD:\nSeven Wonders of the Ancient World', fontsize=16, pad=20, style='italic')
ax.set_xlabel('Wonders of the Ancient World', fontsize=12)
ax.set_ylabel('Number of Tourists (in thousands)', fontsize=12)

plt.xticks(rotation=45, ha='right')

# Modify grid appearance and enable minor grid
ax.yaxis.grid(True, linestyle=':', alpha=0.4)
ax.xaxis.grid(True, which='minor', linestyle='--', alpha=0.2)
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))

# Add a box border around the plot
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['top'].set_color('black')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

plt.tight_layout()
plt.show()