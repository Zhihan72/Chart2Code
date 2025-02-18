import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 25)
cities = ['NY', 'LDN', 'TKY', 'SYD', 'CT']

# Randomly altered temperature data, preserving dimensions
new_york = [0, 2, 3, 9, 13, 22, 25, 24, 18, 13, 7, 5,
            0, 3, 4, 12, 17, 22, 23, 25, 21, 14, 10, 2]
london = [4, 8, 10, 11, 13, 15, 21, 17, 16, 14, 8, 5,
          5, 7, 8, 13, 14, 20, 19, 22, 17, 13, 9, 6]
tokyo = [6, 6, 11, 14, 22, 26, 27, 30, 24, 18, 15, 7,
         5, 8, 13, 17, 20, 26, 28, 28, 25, 19, 14, 10]
sydney = [22, 21, 23, 19, 14, 13, 9, 14, 17, 16, 23, 25,
          23, 22, 23, 18, 17, 12, 12, 15, 17, 20, 22, 24]
cape_town = [26, 22, 22, 19, 16, 11, 11, 12, 16, 18, 21, 22,
             23, 21, 23, 20, 19, 14, 12, 14, 14, 19, 20, 25]

data = [new_york, london, tokyo, sydney, cape_town]

fig, ax = plt.subplots(figsize=(14, 8))
single_color = 'blue'

for temperatures, city in zip(data, cities):
    ax.plot(months, temperatures, color=single_color, label=city)

ax.set_title('Avg Temp Over 2 Years\n(5 Cities)', fontsize=16, fontweight='bold')
ax.set_xlabel('Mon', fontsize=12)
ax.set_ylabel('Temp (°C)', fontsize=12)

ax.set_xticks(months)
ax.set_xticklabels([f'M-{i}' for i in months], rotation=45, ha='right')

ax.legend(loc='lower left', fontsize=10)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()