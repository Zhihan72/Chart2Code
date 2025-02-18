import matplotlib.pyplot as plt

categories = ['Tech Gadgets', 'Apparel', 'Fresh Produce', 'Reading Material', 'Home Essentials']
market_share = [25, 20, 15, 18, 12]
colors = ['#FFA07A', '#20B2AA', '#778899', '#FF6347', '#6A5ACD']
years = ['2018', '2019', '2020', '2021', '2022']
growth_data = {
    'Tech Gadgets': [5, 6, 8, 12, 25],
    'Apparel': [7, 9, 12, 15, 20],
    'Fresh Produce': [6, 7, 9, 12, 15],
    'Reading Material': [8, 10, 12, 15, 18],
    'Home Essentials': [4, 5, 6, 8, 12]
}

fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# Switch the position of pie chart and line plot
for category, data in growth_data.items():
    ax[0].plot(years, data, marker='o')

ax[0].set_title('Evolving Patterns in Digital Retail by Type\nFrom 2018 to 2022', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Calendar Year', fontsize=12)
ax[0].set_ylabel('Portion in Market (%)', fontsize=12)

explode = (0, 0.1, 0, 0, 0)
ax[1].pie(
    market_share, labels=categories, autopct='%1.1f%%', startangle=90, 
    colors=colors, shadow=True, explode=explode, wedgeprops={'width': 0.3}
)
ax[1].set_title('Digital Marketplace Fraction by Type\nAs of 2022', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()