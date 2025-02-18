import matplotlib.pyplot as plt

# Updated market shares with one data group removed
market_shares = [25, 20, 15, 10, 5, 10]
# Updated colors to match the new market shares
new_colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#FF9F40', '#C9CBCF']
# Updated explode to match the new market shares
explode = (0.1, 0, 0, 0, 0, 0)

plt.figure(figsize=(9, 6))
plt.pie(market_shares, autopct='%1.2f%%', startangle=100, 
        colors=new_colors, explode=explode, shadow=False)

plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()