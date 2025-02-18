import matplotlib.pyplot as plt

desserts = ['Cakes', 'Cookies', 'Ice Cream', 'Pastries', 'Pies', 'Donuts']
sales_percentage = [30, 20, 15, 10, 10, 15]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode = (0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(sales_percentage, labels=desserts, autopct='%1.1f%%', startangle=140,
       colors=colors, explode=explode, textprops=dict(color="black", fontsize=12))

plt.setp(autotexts, size=10, weight="bold")

ax.axis('equal')
plt.tight_layout()

plt.show()