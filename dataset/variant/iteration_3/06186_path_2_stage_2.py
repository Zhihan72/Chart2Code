import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
smartphones_sales = [450, 480, 500, 530, 550]
laptops_sales = [300, 320, 350, 380, 400]
tablets_sales = [150, 160, 170, 180, 190]

smartphones_revenue_2022 = 200  # million USD
laptops_revenue_2022 = 250  # million USD
tablets_revenue_2022 = 100  # million USD

bar_width = 0.25
year_indices = np.arange(len(years))

fig, ax = plt.subplots(1, 2, figsize=(16, 8))

colors_bar = ['cornflowerblue', 'mediumseagreen', 'darkorange']
colors_pie = ['steelblue', 'lightgreen', 'sandybrown']

ax[0].bar(year_indices - bar_width, smartphones_sales, width=bar_width, color=colors_bar[0])
ax[0].bar(year_indices, laptops_sales, width=bar_width, color=colors_bar[1])
ax[0].bar(year_indices + bar_width, tablets_sales, width=bar_width, color=colors_bar[2])

ax[0].set_xticks(year_indices)
ax[0].set_xticklabels(years)
ax[0].grid(True, which='major', axis='y', linestyle='--', linewidth=0.5)

revenues_2022 = [smartphones_revenue_2022, laptops_revenue_2022, tablets_revenue_2022]
explode = (0.1, 0, 0)

ax[1].pie(revenues_2022, startangle=140, colors=colors_pie, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

plt.tight_layout()
plt.show()