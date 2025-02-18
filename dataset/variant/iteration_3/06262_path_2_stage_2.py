import matplotlib.pyplot as plt

# Define the data for the pie chart
categories = ['Tech Gadgets', 'Apparel', 'Fresh Produce', 'Reading Material', 'Home Essentials', 'Miscellaneous']
market_share = [25, 20, 15, 18, 12, 10]

# Define colors for each category
colors = ['#FFA07A', '#20B2AA', '#778899', '#FF6347', '#6A5ACD', '#4682B4']

# Data showing the growth of categories over years
years = ['2018', '2019', '2020', '2021', '2022']
growth_data = {
    'Tech Gadgets': [5, 6, 8, 12, 25],
    'Apparel': [7, 9, 12, 15, 20],
    'Fresh Produce': [6, 7, 9, 12, 15],
    'Reading Material': [8, 10, 12, 15, 18],
    'Home Essentials': [4, 5, 6, 8, 12],
    'Miscellaneous': [3, 4, 5, 7, 10]
}

# Set up the figure and axis for subplots
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# Create the donut chart on the first subplot
explode = (0, 0.1, 0, 0, 0, 0)
wedges, texts, autotexts = ax[0].pie(
    market_share, labels=categories, autopct='%1.1f%%', startangle=90, 
    colors=colors, shadow=True, explode=explode, wedgeprops={'edgecolor': 'black', 'width': 0.3}
)
ax[0].set_title('Digital Marketplace Fraction by Type\nAs of 2022', fontsize=14, fontweight='bold', pad=20)

# Create a line chart on the second subplot
for category, data in growth_data.items():
    ax[1].plot(years, data, marker='o', label=category)

ax[1].set_title('Evolving Patterns in Digital Retail by Type\nFrom 2018 to 2022', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Calendar Year', fontsize=12)
ax[1].set_ylabel('Portion in Market (%)', fontsize=12)
ax[1].legend(title="Product Types", loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))
ax[1].grid(True)

plt.tight_layout()
plt.show()