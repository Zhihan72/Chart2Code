import matplotlib.pyplot as plt
import numpy as np

regions = ["Northland", "Southscape", "Eastshore"]
tea_types = ["Black Tea", "Green Tea", "Herbal Tea", "White Tea", "Oolong Tea"]
northland_consumption = [40, 25, 15, 10, 10]
southscape_consumption = [20, 40, 20, 10, 10]
eastshore_consumption = [30, 20, 25, 15, 10]

consumption_data = [northland_consumption, southscape_consumption, eastshore_consumption]

colors = ['#e63946', '#a8dadc', '#1d3557', '#f1faee', '#457b9d']

fig, ax = plt.subplots(1, 3, figsize=(15, 7), subplot_kw=dict(aspect="equal"))

# Shuffling colors for each region's chart without using random module
shuffled_colors = [
    ['#457b9d', '#e63946', '#1d3557', '#a8dadc', '#f1faee'],  # Northland
    ['#f1faee', '#457b9d', '#a8dadc', '#e63946', '#1d3557'],  # Southscape
    ['#1d3557', '#f1faee', '#e63946', '#457b9d', '#a8dadc']   # Eastshore
]

for i, data in enumerate(consumption_data):
    wedges, texts, autotexts = ax[i].pie(
        data, colors=shuffled_colors[i], wedgeprops=dict(width=0.4, edgecolor='w'), startangle=140,
        labels=tea_types, autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="w", fontsize=9)
    )
    for text in texts:
        text.set_color('black')
    ax[i].set_title(f'Tea Preferences in {regions[i]}', fontsize=12, pad=10)
    ax[i].set_xlabel(f'Total: {sum(data)}%', fontsize=10, color='gray')

plt.suptitle("Regional Tea Consumption Preferences", fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()