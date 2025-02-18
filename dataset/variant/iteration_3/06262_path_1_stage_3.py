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

fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# Create the line chart on the first subplot
for data in growth_data.values():
    ax[0].plot(years, data, marker='o', color=single_color)

ax[0].grid(True)

# Create the pie chart on the second subplot
explode = (0, 0.1, 0, 0, 0, 0)
ax[1].pie(market_share, autopct='%1.1f%%', startangle=90, 
          colors=[single_color]*len(market_share), shadow=True, explode=explode, wedgeprops={'edgecolor': 'black'})

plt.tight_layout()
plt.show()