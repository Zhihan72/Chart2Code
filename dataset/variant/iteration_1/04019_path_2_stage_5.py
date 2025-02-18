import matplotlib.pyplot as plt
import numpy as np

continents = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia']
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough']

na_flavors = [15, -25, 35, -12, 13]
eu_flavors = [10, -30, 28, -20, 12]
asia_flavors = [25, -35, 20, -10, 10]
sa_flavors = [15, -20, 25, -10, 30]
africa_flavors = [10, -25, 30, -20, 15]
australia_flavors = [20, -10, 15, -25, 30]

flavor_data = [na_flavors, eu_flavors, asia_flavors, sa_flavors, africa_flavors, australia_flavors]

colors = ['#fc5a8d', '#c0c0c0', '#98ff98', '#f3e5ab', '#8b4513']

# Changed subplot arrangement to 2 rows and 1 column with the same total number of subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 16))

bottoms_pos = np.zeros(len(continents))
bottoms_neg = np.zeros(len(continents))
for idx, flavor in enumerate(flavors):
    pos_values = [data[idx] if data[idx] > 0 else 0 for data in flavor_data]
    neg_values = [data[idx] if data[idx] < 0 else 0 for data in flavor_data]
    
    ax1.bar(continents, pos_values, bottom=bottoms_pos, color=colors[idx], edgecolor='black', alpha=0.7)
    ax1.bar(continents, neg_values, bottom=bottoms_neg, color=colors[idx], edgecolor='black', alpha=0.7)
    
    bottoms_pos += pos_values
    bottoms_neg += neg_values

ax1.axhline(y=0, color='black', linewidth=0.8)
ax1.set_xlabel("Continents", fontsize=12)
ax1.set_ylabel("Popularity Percentage (%)", fontsize=12)

years = np.arange(2013, 2024)
vanilla_growth = [20, 23, 22, 34, 26, 27, 30, 29, 32, 25, 33]

ax2.plot(years, vanilla_growth, marker='o', linestyle='-', color='#f3e5ab', linewidth=2, markersize=6)

for i, growth in enumerate(vanilla_growth):
    ax2.text(years[i], growth + 0.5, f'{growth}%', ha='center', fontsize=10)

ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Popularity Percentage (%)", fontsize=12)

fig.tight_layout()
plt.show()