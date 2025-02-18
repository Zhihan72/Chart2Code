import matplotlib.pyplot as plt
import numpy as np

regions = ["Sahara", "Iceberg"]
tea_types = ["Herbal Tea", "Green Tea", "Black Tea", "Oolong Tea"]
consumption_sahara = [15, 25, 10, 40]
consumption_iceberg = [20, 10, 40, 30]

consumption_data = [consumption_sahara, consumption_iceberg]
shuffled_colors = ['#457b9d', '#e63946', '#a8dadc', '#1d3557']

fig, ax = plt.subplots(1, 2, figsize=(10, 7), subplot_kw=dict(aspect="equal"))

for i, data in enumerate(consumption_data):
    wedges, texts, autotexts = ax[i].pie(
        data, colors=shuffled_colors, wedgeprops=dict(width=0.4, edgecolor='w'), startangle=140,
        labels=tea_types, autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="w", fontsize=9)
    )
    for text in texts:
        text.set_color('black')
    ax[i].set_title(f'Favorite Teas in {regions[i]}', fontsize=12, pad=10)
    ax[i].set_xlabel(f'Aggregate: {sum(data)}%', fontsize=10, color='gray')

plt.suptitle("Comparative Tea Preferences", fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()