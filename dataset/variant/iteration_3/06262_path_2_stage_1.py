import matplotlib.pyplot as plt

# Define the data for the pie chart
categories = ['Books', 'Electronics', 'Clothing', 'Groceries', 'Household Items', 'Others']
market_share = [25, 20, 15, 18, 12, 10]

# Define colors for each category
colors = ['#FFA07A', '#20B2AA', '#778899', '#FF6347', '#6A5ACD', '#4682B4']

# Data showing the growth of categories over years
years = ['2018', '2019', '2020', '2021', '2022']
growth_data = {
    'Books': [5, 6, 8, 12, 25],
    'Electronics': [7, 9, 12, 15, 20],
    'Clothing': [6, 7, 9, 12, 15],
    'Groceries': [8, 10, 12, 15, 18],
    'Household Items': [4, 5, 6, 8, 12],
    'Others': [3, 4, 5, 7, 10]
}

# Set up the figure and axis for subplots
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# Create the donut chart on the first subplot
explode = (0, 0.1, 0, 0, 0, 0)
wedges, texts, autotexts = ax[0].pie(
    market_share, labels=categories, autopct='%1.1f%%', startangle=90, 
    colors=colors, shadow=True, explode=explode, wedgeprops={'edgecolor': 'black', 'width': 0.3}
)
ax[0].set_title('E-commerce Market Share by Category\nYear 2022', fontsize=14, fontweight='bold', pad=20)

# Create a line chart on the second subplot to show growth over years
for category, data in growth_data.items():
    ax[1].plot(years, data, marker='o', label=category)

ax[1].set_title('Growth in E-commerce Market Share by Category\n2018-2022', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Market Share (%)', fontsize=12)
ax[1].legend(title="Categories", loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))
ax[1].grid(True)

# Ensure layout is adjusted to prevent overlap
plt.tight_layout()

# Display the combined chart
plt.show()