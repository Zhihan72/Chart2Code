import matplotlib.pyplot as plt
import numpy as np

# Data (in thousands of units)
years = ['2018', '2019', '2020', '2021', '2022']
smartphones_sales = [450, 480, 500, 530, 550]
laptops_sales = [300, 320, 350, 380, 400]

# Overall revenue contribution in 2022 (in millions USD)
smartphones_revenue_2022 = 200  # million USD
laptops_revenue_2022 = 250  # million USD

# Bar positions
bar_width = 0.35
year_indices = np.arange(len(years))

# Creating the figure and subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Bar chart of sales over the years
ax[0].bar(year_indices - bar_width/2, smartphones_sales, width=bar_width, color='royalblue', label='Smartphones')
ax[0].bar(year_indices + bar_width/2, laptops_sales, width=bar_width, color='seagreen', label='Laptops')

ax[0].set_title('Annual Sales of Tech Gadgets (2018-2022)', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Units Sold (Thousands)', fontsize=12)
ax[0].set_xticks(year_indices)
ax[0].set_xticklabels(years)
ax[0].legend(title='Gadget Type', fontsize=10, title_fontsize='12')
ax[0].grid(True, which='major', axis='y', linestyle='--', linewidth=0.5)

# Annotating Sales Figures
for i in range(len(years)):
    ax[0].text(year_indices[i] - bar_width/2, smartphones_sales[i] + 10, f'{smartphones_sales[i]}', ha='center', color='royalblue')
    ax[0].text(year_indices[i] + bar_width/2, laptops_sales[i] + 10, f'{laptops_sales[i]}', ha='center', color='seagreen')

# Second subplot: Pie chart of revenue contribution in 2022
revenues_2022 = [smartphones_revenue_2022, laptops_revenue_2022]
labels = ['Smartphones', 'Laptops']
colors = ['royalblue', 'seagreen']
explode = (0.1, 0)  # emphasize the highest contributor

ax[1].pie(revenues_2022, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
ax[1].set_title('Revenue Contribution by Gadget Type in 2022', fontsize=14, fontweight='bold')

# Tight layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()