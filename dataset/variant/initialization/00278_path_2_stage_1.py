import matplotlib.pyplot as plt
import numpy as np

wonders = [
    "Great Pyramid of Giza", "Hanging Gardens of Babylon",
    "Statue of Zeus at Olympia", "Temple of Artemis at Ephesus",
    "Mausoleum at Halicarnassus", "Colossus of Rhodes", 
    "Lighthouse of Alexandria"
]

tourists = np.array([450, 380, 270, 310, 200, 290, 410])

# New set of colors for each wonder
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(wonders, tourists, color=new_colors, edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval}k', ha='center', va='bottom', fontsize=10, color='black')

ax.set_title('Tourist Attraction in 100 AD:\nSeven Wonders of the Ancient World', fontsize=16, pad=20)
ax.set_xlabel('Wonders of the Ancient World', fontsize=12)
ax.set_ylabel('Number of Tourists (in thousands)', fontsize=12)

plt.xticks(rotation=45, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()