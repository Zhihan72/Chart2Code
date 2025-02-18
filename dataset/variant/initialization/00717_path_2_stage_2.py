import matplotlib.pyplot as plt

market_shares = [25, 20, 15, 10, 15, 5, 10]
colors = ['#6B4226', '#C5A880', '#FF9999', '#FFCC99', '#66B3FF', '#99FF99', '#FF6666']
explode = (0.1, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(9, 6))
plt.pie(market_shares, autopct='%1.2f%%', startangle=100, 
        colors=colors, explode=explode, shadow=False,)

plt.axis('equal')

plt.grid(True)
plt.tight_layout()

plt.show()