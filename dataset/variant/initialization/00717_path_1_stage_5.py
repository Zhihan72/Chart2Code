import matplotlib.pyplot as plt

beverage_categories = ['Mocktails', 'Coffee', 'Juices', 'Bottled Water', 'Energy Drinks', 'Smoothies', 'Alcoholic Beverages', 'Tea', 'Soft Drinks']
market_shares = [25, 20, 15, 10, 15, 5, 10, 5, 5]

# Manually shuffled colors
colors = ['#FF6666', '#FFCC99', '#C5A880', '#6B4226', '#66B3FF', '#91a832', '#c883fb', '#99FF99', '#FF9999']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
plt.pie(market_shares, labels=beverage_categories, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True, wedgeprops=dict(width=0.3))

plt.title('Global Beverage Preferences Study\n(2023)', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')

plt.show()