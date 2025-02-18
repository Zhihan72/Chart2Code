import matplotlib.pyplot as plt

beverage_categories = ['Coffee', 'Tea', 'Soft Drinks', 'Energy Drinks', 'Bottled Water', 'Juices', 'Alcoholic Beverages']
market_shares = [25, 20, 15, 10, 15, 5, 10]
colors = ['#6B4226', '#C5A880', '#FF9999', '#FFCC99', '#66B3FF', '#99FF99', '#FF6666']
explode = (0.1, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(9, 6))
plt.pie(market_shares, labels=beverage_categories, autopct='%1.2f%%', startangle=100, 
        colors=colors, explode=explode, shadow=False,)

plt.title('Beverage Consumption Preferences Worldwide\n(2023)', fontsize=18, fontweight='light', pad=10)
plt.axis('equal')

plt.legend(beverage_categories, title="Categories", loc='lower left', bbox_to_anchor=(-0.2, 0.5), frameon=False)

plt.grid(True)
plt.tight_layout()

plt.show()