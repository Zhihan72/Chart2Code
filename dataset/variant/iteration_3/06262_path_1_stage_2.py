import matplotlib.pyplot as plt

# Define the data for the pie chart
market_share = [25, 20, 15, 18, 12, 10]

# Choose a consistent color for all data groups
single_color = '#20B2AA'  # Light Sea Green

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

# Create the pie chart on the first subplot
explode = (0, 0.1, 0, 0, 0, 0)
ax[0].pie(market_share, autopct='%1.1f%%', startangle=90, 
          colors=[single_color]*len(market_share), shadow=True, explode=explode, wedgeprops={'edgecolor': 'black'})

# Create a line chart on the second subplot to show growth over years
for data in growth_data.values():
    ax[1].plot(years, data, marker='o', color=single_color)

ax[1].grid(True)

# Ensure layout is adjusted to prevent overlap
plt.tight_layout()

# Display the combined chart
plt.show()