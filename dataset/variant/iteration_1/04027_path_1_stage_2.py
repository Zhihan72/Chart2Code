import matplotlib.pyplot as plt
import numpy as np

comic_series = [
    'The Valiant Avenger',
    'Cosmic Defender',
    'Mystery Sleuth',
    'Dark Knight',
    'Fast & Fearless',
    'Captain Marvelous',
    'The Spectrum Enigma'
]
annual_profits = [85, 75, 60, 95, 70, 50, 65]

fig, ax = plt.subplots(figsize=(12, 8))
single_color = '#1e90ff'

bars = ax.barh(np.arange(len(comic_series)), annual_profits, color=single_color, height=0.7, alpha=0.85)

for bar in bars:
    ax.annotate(f"${bar.get_width()}M", 
                 xy=(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2),
                 va='center', ha='left', color='black', fontsize=12, fontweight='bold')

ax.set_xlabel('Annual Profit (in Millions USD)', fontsize=14)
ax.set_yticks(np.arange(len(comic_series)))
ax.set_yticklabels(comic_series, fontsize=12)

ax.invert_yaxis()

plt.tight_layout()
plt.show()