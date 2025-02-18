import matplotlib.pyplot as plt
import numpy as np

years = list(range(2010, 2021))
playstation_sales = [14.2, 13.3, 16.3, 14.9, 17.8, 18.5, 19.4, 20.0, 17.7, 14.4, 12.5]
xbox_sales = [10.3, 9.4, 11.6, 12.7, 13.8, 15.3, 14.7, 16.2, 15.4, 14.1, 13.5]
nintendo_sales = [8.8, 9.0, 10.7, 11.8, 12.3, 13.7, 16.3, 15.4, 14.2, 18.5, 20.1]

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