import matplotlib.pyplot as plt

desserts = ['Ice Cream', 'Cookies', 'Cakes', 'Donuts', 'Pies', 'Pastries']
sales_percentage = [15, 20, 30, 15, 10, 10]

colors = ['#99ff99', '#66b3ff', '#ff9999', '#ffb3e6', '#c2c2f0', '#ffcc99']
explode = (0, 0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sales_percentage, labels=desserts, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, textprops=dict(color="black", fontsize=12))

# Creating a donut shape by drawing a circle at the center of the pie chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

ax.axis('equal')  
plt.tight_layout()

plt.show()