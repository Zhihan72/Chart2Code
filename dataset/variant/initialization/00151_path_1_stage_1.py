import matplotlib.pyplot as plt
import numpy as np

genres = ['Action', 'RPG', 'Strategy', 'Sports', 'Shooter', 'Simulation']
market_shares = [25, 20, 15, 15, 12, 8]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
patterns = ['/', '\\', '|', '-', '+', 'x']

explode = (0.1, 0.05, 0, 0, 0, 0)

fig, axs = plt.subplots(2, 1, figsize=(12, 12))
fig.suptitle('Video Game Genre Market Analysis in 2023', fontsize=18, weight='bold', y=0.95)

wedges, texts, autotexts = axs[0].pie(
    market_shares, explode=explode, labels=genres, autopct='%1.1f%%', startangle=140,
    colors=colors, wedgeprops=dict(edgecolor='w', linewidth=1.5, linestyle='-', 
    alpha=0.9), shadow=True
)

for i, wedge in enumerate(wedges):
    wedge.set_hatch(patterns[i])

plt.setp(texts, size=10)
plt.setp(autotexts, size=11, color='white', weight='bold')

axs[0].set_title('Market Share by Genre', fontsize=14, pad=15)
axs[0].axis('equal')
axs[0].legend(wedges, genres, title="Genres", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

years = [2020, 2021, 2022, 2023]
action_trend = [20, 22, 24, 25]
rpg_trend = [18, 19, 19.5, 20]

axs[1].bar(years, action_trend, color='#ff9999', alpha=0.7, label='Action')
axs[1].bar(years, rpg_trend, color='#66b3ff', alpha=0.7, label='RPG', bottom=action_trend)

axs[1].set_title('Market Share Trends (Action vs. RPG)', fontsize=14, pad=10)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Market Share (%)', fontsize=12)
axs[1].legend(loc='upper left')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()