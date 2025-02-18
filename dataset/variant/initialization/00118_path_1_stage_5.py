import matplotlib.pyplot as plt

regions = ["Northern Land", "Shore of the East"]
tea_types = ["Brewing Black", "Leaves of Green", "Herbal Infusion", "White Leaves", "Oolong Aroma"]
northland_consumption = [40, 25, 15, 10, 10]
eastshore_consumption = [30, 20, 25, 15, 10]

consumption_data = [northland_consumption, eastshore_consumption]

fig, ax = plt.subplots(1, 2, figsize=(10, 5), subplot_kw=dict(aspect="equal"))
ax = ax.flatten()

shuffled_colors = [
    ['#457b9d', '#e63946', '#1d3557', '#a8dadc', '#f1faee'],
    ['#1d3557', '#f1faee', '#e63946', '#457b9d', '#a8dadc']
]

for i, data in enumerate(consumption_data):
    ax[i].pie(
        data, colors=shuffled_colors[i], wedgeprops=dict(width=0.4), startangle=140,
        autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="w", fontsize=9)
    )
    ax[i].set_title(f'Flavor Favors in {regions[i]}', fontsize=12, pad=10)
    ax[i].set_xlabel(f'Total Enjoyment: {sum(data)}%', fontsize=10, color='gray')

plt.suptitle("Cultural Infusion Preferences", fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()