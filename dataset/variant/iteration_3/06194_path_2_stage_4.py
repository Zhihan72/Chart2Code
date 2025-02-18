import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 25)

new_york_city = [0, 1, 7, 10, 11, 26, 24, 21, 19, 14, 8, 3, 
                 1, 0, 5, 12, 16, 21, 28, 24, 20, 13, 9, 4]
london_town = [8, 3, 8, 11, 18, 16, 19, 20, 13, 15, 9, 4, 
               6, 3, 9, 18, 15, 13, 21, 19, 15, 17, 12, 5]
tokyo_city = [5, 10, 10, 9, 22, 20, 28, 31, 19, 23, 14, 7, 
              6, 12, 11, 10, 23, 25, 29, 27, 22, 20, 14, 8]
sydney_land = [24, 21, 19, 18, 16, 11, 12, 13, 17, 14, 22, 22, 
               20, 24, 18, 20, 15, 10, 16, 13, 12, 18, 21, 23]
cape_town_zone = [24, 18, 21, 20, 12, 16, 10, 11, 14, 19, 18, 22, 
                  25, 21, 22, 16, 12, 11, 13, 17, 14, 20, 21, 24]

data = [new_york_city, london_town, tokyo_city, sydney_land, cape_town_zone]
colors = ['red', 'blue', 'green', 'purple', 'orange']

fig, ax = plt.subplots(figsize=(14, 8))

for temperatures, color in zip(data, colors):
    ax.plot(months, temperatures, color=color, marker='o')

ax.set_title('Climatic Trends for 5 Cities Over Two-Year Span', fontsize=16, fontweight='bold')
ax.set_xlabel('Month of Year', fontsize=12)
ax.set_ylabel('Temp (°C)', fontsize=12)
ax.set_xticks(months)
ax.set_xticklabels([f'Mth-{i}' for i in months], rotation=45, ha='right')

plt.tight_layout()
plt.show()