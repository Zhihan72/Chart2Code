import matplotlib.pyplot as plt
import numpy as np

years = list(range(2010, 2021))
# Manually shuffled data for each sales group
playstation_sales = [16.3, 13.3, 17.8, 12.5, 18.5, 19.4, 14.2, 14.4, 20.0, 14.9, 17.7]
xbox_sales = [13.8, 10.3, 11.6, 15.4, 9.4, 16.2, 14.1, 12.7, 13.5, 15.3, 14.7]
nintendo_sales = [12.3, 11.8, 10.7, 9.0, 15.4, 16.3, 8.8, 20.1, 13.7, 18.5, 14.2]

fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.25
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

ax.barh(r1, playstation_sales, color='blue', height=bar_width, edgecolor='green', linestyle='-.')
ax.barh(r2, xbox_sales, color='red', height=bar_width, edgecolor='yellow', linestyle=':')
ax.barh(r3, nintendo_sales, color='pink', height=bar_width, edgecolor='darkblue', linestyle='--')

plt.grid(axis='x', linestyle='-', linewidth=0.8, color='grey', alpha=0.5)

ax.set_yticks([r + bar_width for r in range(len(years))])
ax.set_yticklabels(years)
ax.legend(['PlayStation', 'Xbox', 'Nintendo'], loc='lower right', frameon=True, shadow=True)

plt.tight_layout()
plt.show()