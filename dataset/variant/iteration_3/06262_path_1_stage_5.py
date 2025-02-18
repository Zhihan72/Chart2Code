import matplotlib.pyplot as plt

market_share = [25, 20, 15, 18, 12]
single_color = '#20B2AA'

years = ['2018', '2019', '2020', '2021', '2022']
growth_data = {
    'Books': [5, 6, 8, 12, 25],
    'Electronics': [7, 9, 12, 15, 20],
    'Clothing': [6, 7, 9, 12, 15],
    'Groceries': [8, 10, 12, 15, 18],
    'Household Items': [4, 5, 6, 8, 12]
}

fig, ax = plt.subplots(1, 2, figsize=(18, 8))

for data in growth_data.values():
    ax[0].plot(years, data, marker='o', color=single_color)

# Create pie chart without shadow and explode effects
ax[1].pie(market_share, autopct='%1.1f%%', startangle=90, 
          colors=[single_color]*len(market_share))

plt.tight_layout()
plt.show()