import matplotlib.pyplot as plt
import numpy as np

# Backstory: 
# A tech company tracks its annual sales of different types of tech gadgets over the last 5 years. 
# The company sells three main types of gadgets: Smartphones, Laptops, and Tablets.
# We will visualize this data using a bar chart to understand the sales trends over the years and also introduce a subplot showing the overall revenue contribution of each gadget type in the latest year.

# Data (in thousands of units)
years = ['2018', '2019', '2020', '2021', '2022']
smartphones_sales = [450, 480, 500, 530, 550]
laptops_sales = [300, 320, 350, 380, 400]
tablets_sales = [150, 160, 170, 180, 190]

# Overall revenue contribution in 2022 (in millions USD)
smartphones_revenue_2022 = 200  # million USD
laptops_revenue_2022 = 250  # million USD
tablets_revenue_2022 = 100  # million USD

# Bar positions
bar_width = 0.25
year_indices = np.arange(len(years))

# Creating the figure and subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Bar chart of sales over the years
ax[0].bar(year_indices - bar_width, smartphones_sales, width=bar_width, color='royalblue', label='Smartphones')
ax[0].bar(year_indices, laptops_sales, width=bar_width, color='seagreen', label='Laptops')
ax[0].bar(year_indices + bar_width, tablets_sales, width=bar_width, color='orange', label='Tablets')

ax[0].set_title('Annual Sales of Tech Gadgets (2018-2022)', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Units Sold (Thousands)', fontsize=12)
ax[0].set_xticks(year_indices)
ax[0].set_xticklabels(years)
ax[0].legend(title='Gadget Type', fontsize=10, title_fontsize='12')
ax[0].grid(True, which='major', axis='y', linestyle='--', linewidth=0.5)

# Annotating Sales Figures
for i in range(len(years)):
    ax[0].text(year_indices[i] - bar_width, smartphones_sales[i] + 10, f'{smartphones_sales[i]}', ha='center', color='royalblue')
    ax[0].text(year_indices[i], laptops_sales[i] + 10, f'{laptops_sales[i]}', ha='center', color='seagreen')
    ax[0].text(year_indices[i] + bar_width, tablets_sales[i] + 10, f'{tablets_sales[i]}', ha='center', color='orange')

# Second subplot: Pie chart of revenue contribution in 2022
revenues_2022 = [smartphones_revenue_2022, laptops_revenue_2022, tablets_revenue_2022]
labels = ['Smartphones', 'Laptops', 'Tablets']
colors = ['royalblue', 'seagreen', 'orange']
explode = (0.1, 0, 0)  # emphasize the highest contributor

ax[1].pie(revenues_2022, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
ax[1].set_title('Revenue Contribution by Gadget Type in 2022', fontsize=14, fontweight='bold')

# Tight layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()