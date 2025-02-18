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

# New color palette
colors_bar = ['cornflowerblue', 'mediumseagreen', 'darkorange']
colors_pie = ['steelblue', 'lightgreen', 'sandybrown']

ax[0].bar(year_indices - bar_width, smartphones_sales, width=bar_width, color=colors_bar[0], label='Smartphones')
ax[0].bar(year_indices, laptops_sales, width=bar_width, color=colors_bar[1], label='Laptops')
ax[0].bar(year_indices + bar_width, tablets_sales, width=bar_width, color=colors_bar[2], label='Tablets')

ax[0].set_title('Annual Sales of Tech Gadgets (2018-2022)', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Units Sold (Thousands)', fontsize=12)
ax[0].set_xticks(year_indices)
ax[0].set_xticklabels(years)
ax[0].legend(title='Gadget Type', fontsize=10, title_fontsize='12')
ax[0].grid(True, which='major', axis='y', linestyle='--', linewidth=0.5)

for i in range(len(years)):
    ax[0].text(year_indices[i] - bar_width, smartphones_sales[i] + 10, f'{smartphones_sales[i]}', ha='center', color=colors_bar[0])
    ax[0].text(year_indices[i], laptops_sales[i] + 10, f'{laptops_sales[i]}', ha='center', color=colors_bar[1])
    ax[0].text(year_indices[i] + bar_width, tablets_sales[i] + 10, f'{tablets_sales[i]}', ha='center', color=colors_bar[2])

revenues_2022 = [smartphones_revenue_2022, laptops_revenue_2022, tablets_revenue_2022]
labels = ['Smartphones', 'Laptops', 'Tablets']
explode = (0.1, 0, 0)

ax[1].pie(revenues_2022, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors_pie, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
ax[1].set_title('Revenue Contribution by Gadget Type in 2022', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()