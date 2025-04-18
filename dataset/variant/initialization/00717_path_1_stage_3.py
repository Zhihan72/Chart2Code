import matplotlib.pyplot as plt

beverage_categories = ['Coffee', 'Tea', 'Soft Drinks', 'Energy Drinks', 'Bottled Water', 'Juices', 'Alcoholic Beverages', 'Mocktails', 'Smoothies']
market_shares = [25, 20, 15, 10, 15, 5, 10, 5, 5]

colors = ['#6B4226', '#C5A880', '#FF9999', '#FFCC99', '#66B3FF', '#99FF99', '#FF6666', '#91a832', '#c883fb']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
plt.pie(market_shares, labels=beverage_categories, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True, wedgeprops=dict(width=0.3))

plt.title('Beverage Consumption Preferences Worldwide\n(2023)', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')

plt.show()