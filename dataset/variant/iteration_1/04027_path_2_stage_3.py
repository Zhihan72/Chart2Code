import matplotlib.pyplot as plt
import numpy as np

comic_series = [
    'Valiant Avenger',
    'Cosmic Defender',
    'Mystery Sleuth',
    'Dark Knight',
    'Fast & Fearless',
    'Captain Marvelous',
    'Spectrum Enigma'
]
annual_profits = [85, 75, 60, 95, 70, 50, 65]

fig, ax = plt.subplots(figsize=(12, 8))

# This section is where we make changes to the stylistic elements:

# Altered colors for variation
colors = ['#FF4500', '#ADFF2F', '#FFD700', '#B22222', '#7FFF00', '#DC143C', '#00FA9A']

# Changed the edge color and adjusted the bar transparency
bars = ax.barh(np.arange(len(comic_series)), annual_profits, color=colors, edgecolor='purple', height=0.6, alpha=0.75)

# Updated text color and size
for bar in bars:
    ax.annotate(f"${bar.get_width()}M", 
                 xy=(bar.get_width() - 1, bar.get_y() + bar.get_height() / 2),
                 va='center', ha='right', color='blue', fontsize=10, fontweight='bold')

ax.set_title('2025 Top Comic Series Profits', fontsize=20, fontweight='bold', color='darkgreen')
ax.set_xlabel('Profit (Millions USD)', fontsize=13)
ax.set_yticks(np.arange(len(comic_series)))
ax.set_yticklabels(comic_series, fontsize=11)

# Adjusted grid line properties
ax.grid(axis='x', linestyle='-.', alpha=0.4)

# Changed aesthetic elements
ax.spines['bottom'].set_color('orchid')
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_visible(False)

# Changed marker for highlighting
max_profit = max(annual_profits)
max_profit_series = comic_series[annual_profits.index(max_profit)]

ax.plot([max_profit], [annual_profits.index(max_profit)], 'bs')  # blue square marker
ax.annotate(f"Highest\n{max_profit_series}: ${max_profit}M",
             xy=(max_profit, annual_profits.index(max_profit)),
             xytext=(max_profit+8, annual_profits.index(max_profit)-0.4),
             arrowprops=dict(facecolor='purple', shrink=0.05),
             fontsize=11, color='green', fontweight='bold', ha='left')

plt.tight_layout()
plt.show()