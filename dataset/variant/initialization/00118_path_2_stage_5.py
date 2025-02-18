import matplotlib.pyplot as plt

regions = ["Sahara", "Iceberg"]
tea_types = ["Herbal Tea", "Green Tea", "Black Tea", "Oolong Tea"]
consumption_sahara = [15, 25, 10, 40]
consumption_iceberg = [20, 10, 40, 30]

consumption_data = [consumption_sahara, consumption_iceberg]
shuffled_colors = ['#457b9d', '#e63946', '#a8dadc', '#1d3557']

fig, ax = plt.subplots(1, 2, figsize=(10, 7), subplot_kw=dict(aspect="equal"))

for i, data in enumerate(consumption_data):
    ax[i].pie(
        data, colors=shuffled_colors, wedgeprops=dict(width=0.4, edgecolor='w'), startangle=140,
        labels=tea_types, autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="black", fontsize=9)
    )
    ax[i].set_title(f'Favorite Teas in {regions[i]}', fontsize=12, pad=10)

plt.subplots_adjust(top=0.92)

plt.show()