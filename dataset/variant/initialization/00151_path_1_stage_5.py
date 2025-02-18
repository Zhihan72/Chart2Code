import matplotlib.pyplot as plt
import numpy as np

genres = ['Adventure', 'Puzzle', 'Arcade', 'Racing', 'Shooter', 'Strategy']
market_shares = [25, 20, 15, 15, 12, 8]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
patterns = ['/', '\\', '|', '-', '+', 'x']

explode = (0.1, 0.05, 0, 0, 0, 0)

fig, axs = plt.subplots(2, 1, figsize=(12, 12))
fig.suptitle('Digital Entertainment Genre Report in 2023', fontsize=18, weight='bold', y=0.95)

years = [2020, 2021, 2022, 2023]
action_trend = [20, 22, 24, 25]
rpg_trend = [18, 19, 19.5, 20]

axs[0].bar(years, action_trend, color='#ff9999', alpha=0.7)
axs[0].bar(years, rpg_trend, color='#66b3ff', alpha=0.7, bottom=action_trend)

axs[0].set_xlabel('Timeline (Years)', fontsize=12)
axs[0].set_ylabel('Percentage of Interest (%)', fontsize=12)

wedges, texts, autotexts = axs[1].pie(
    market_shares, explode=explode, labels=genres, autopct='%1.1f%%', startangle=140,
    colors=colors, wedgeprops=dict(width=0.3, edgecolor='w', linewidth=1.5, linestyle='-', 
    alpha=0.9)
)

for i, wedge in enumerate(wedges):
    wedge.set_hatch(patterns[i])

plt.setp(texts, size=10)
plt.setp(autotexts, size=11, color='white', weight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()