import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
smartphones_sales = [450, 480, 500, 530, 550]
laptops_sales = [300, 320, 350, 380, 400]
tablets_sales = [150, 160, 170, 180, 190]
wearables_sales = [50, 60, 70, 80, 90]  # New data series for wearables

smartphones_revenue_2022 = 200
laptops_revenue_2022 = 250
tablets_revenue_2022 = 100
wearables_revenue_2022 = 50  # Revenue for wearables in 2022

bar_width = 0.2  # Adjusted bar width to fit the additional category
year_indices = np.arange(len(years))

fig, ax = plt.subplots(2, 1, figsize=(10, 12))  # Changed to 2x1 grid

colors_bar = ['cornflowerblue', 'mediumseagreen', 'darkorange', 'mediumvioletred']
colors_pie = ['steelblue', 'lightgreen', 'sandybrown', 'orchid']

ax[0].bar(year_indices - 1.5*bar_width, smartphones_sales, width=bar_width, color=colors_bar[0])
ax[0].bar(year_indices - 0.5*bar_width, laptops_sales, width=bar_width, color=colors_bar[1])
ax[0].bar(year_indices + 0.5*bar_width, tablets_sales, width=bar_width, color=colors_bar[2])
ax[0].bar(year_indices + 1.5*bar_width, wearables_sales, width=bar_width, color=colors_bar[3])  # New wearables bar

ax[0].set_xticks(year_indices)
ax[0].set_xticklabels(years)

revenues_2022 = [smartphones_revenue_2022, laptops_revenue_2022, tablets_revenue_2022, wearables_revenue_2022]
explode = (0.1, 0, 0, 0)  # Slightly modify explode for visual clarity

ax[1].pie(revenues_2022, startangle=140, colors=colors_pie, explode=explode, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

plt.tight_layout()
plt.show()