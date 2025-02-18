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

# New set of colors for the bars
colors = ['#6495ED', '#FF69B4', '#8A2BE2', '#00CED1', '#FFD700', '#32CD32', '#4169E1']

bars = ax.barh(np.arange(len(comic_series)), annual_profits, color=colors, edgecolor='purple', height=0.6, alpha=0.75)

for bar in bars:
    ax.annotate(f"${bar.get_width()}M", 
                 xy=(bar.get_width() - 1, bar.get_y() + bar.get_height() / 2),
                 va='center', ha='right', color='blue', fontsize=10, fontweight='bold')

ax.set_title('2025 Top Comic Series Profits', fontsize=20, fontweight='bold', color='darkgreen')
ax.set_xlabel('Profit (Millions USD)', fontsize=13)
ax.set_yticks(np.arange(len(comic_series)))
ax.set_yticklabels(comic_series, fontsize=11)

ax.grid(axis='x', linestyle='-.', alpha=0.4)

ax.spines['bottom'].set_color('orchid')
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_visible(False)

max_profit = max(annual_profits)
max_profit_series = comic_series[annual_profits.index(max_profit)]

ax.plot([max_profit], [annual_profits.index(max_profit)], 'bs')
ax.annotate(f"Highest\n{max_profit_series}: ${max_profit}M",
             xy=(max_profit, annual_profits.index(max_profit)),
             xytext=(max_profit+8, annual_profits.index(max_profit)-0.4),
             arrowprops=dict(facecolor='purple', shrink=0.05),
             fontsize=11, color='green', fontweight='bold', ha='left')

plt.tight_layout()
plt.show()