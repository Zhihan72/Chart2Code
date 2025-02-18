import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
smartphones_sales = [450, 480, 500, 530, 550]
laptops_sales = [300, 320, 350, 380, 400]

smartphones_revenue_2022 = 200
laptops_revenue_2022 = 250

bar_width = 0.35
year_indices = np.arange(len(years))

fig, ax = plt.subplots(2, 1, figsize=(10, 12))

# First subplot
ax[0].bar(year_indices - bar_width/2, smartphones_sales, width=bar_width, color='seagreen', label='Phones')
ax[0].bar(year_indices + bar_width/2, laptops_sales, width=bar_width, color='royalblue', label='Computers')

ax[0].set_title('Sales Overview (2018-2022)', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Fiscal Year', fontsize=12)
ax[0].set_ylabel('Units (K)', fontsize=12)
ax[0].set_xticks(year_indices)
ax[0].set_xticklabels(['18', '19', '20', '21', '22'])  # Shortened year labels for variety
ax[0].legend(title='Device Category', fontsize=10, title_fontsize='12')
ax[0].grid(True, which='major', axis='y', linestyle='--', linewidth=0.5)

for i in range(len(years)):
    ax[0].text(year_indices[i] - bar_width/2, smartphones_sales[i] + 10, f'{smartphones_sales[i]}K', ha='center', color='seagreen')
    ax[0].text(year_indices[i] + bar_width/2, laptops_sales[i] + 10, f'{laptops_sales[i]}K', ha='center', color='royalblue')

# Second subplot
revenues_2022 = [smartphones_revenue_2022, laptops_revenue_2022]
labels = ['Phones', 'Computers']
colors = ['seagreen', 'royalblue']
explode = (0.1, 0)

ax[1].pie(revenues_2022, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
ax[1].set_title('2022 Revenue Breakdown by Device', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()