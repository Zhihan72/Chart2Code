import matplotlib.pyplot as plt
import numpy as np

# Original data
comic_series = [
    'Valiant Avenger',
    'Cosmic Defender',
    'Mystery Sleuth',
    'Dark Knight',
    'Fast & Fearless',
    'Spectrum Enigma'
]
annual_profits = [85, 75, 60, 95, 70, 65]

# Sort the data in descending order
sorted_indices = np.argsort(annual_profits)[::-1]
comic_series_sorted = [comic_series[i] for i in sorted_indices]
annual_profits_sorted = [annual_profits[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))
single_color = '#1e90ff'

bars = ax.barh(np.arange(len(comic_series_sorted)), annual_profits_sorted, color=single_color, height=0.7, alpha=0.85)

for bar in bars:
    ax.annotate(f"${bar.get_width()}M", 
                 xy=(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2),
                 va='center', ha='left', color='black', fontsize=12, fontweight='bold')

ax.set_xlabel('Profit (Millions USD)', fontsize=14)
ax.set_yticks(np.arange(len(comic_series_sorted)))
ax.set_yticklabels(comic_series_sorted, fontsize=12)

ax.invert_yaxis()

plt.tight_layout()
plt.show()