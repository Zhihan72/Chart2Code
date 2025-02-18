import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
coffee_varieties = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']

sales_data = np.array([
    [200, 150, 220, 180, 250],
    [260, 210, 180, 230, 190],
    [230, 220, 270, 200, 250],
    [250, 300, 240, 210, 230],
    [320, 270, 260, 220, 250],
    [270, 290, 240, 330, 270]
])

average_sales = sales_data.mean(axis=1)

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['#A0522D', '#D2691E', '#8B4513', '#CD853F', '#DEB887']
dx = dy = 0.5

for y, color in enumerate(colors):
    xs = np.arange(len(months))
    ys = sales_data[:, y]
    ax.bar3d(xs, y, np.zeros_like(xs), dx, dy, ys, color=color, alpha=0.8)

ax.plot(np.arange(len(months)), [-0.5] * len(months), average_sales, color='navy', marker='o', linewidth=2)

ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45)
ax.set_yticks(np.arange(len(coffee_varieties)))
ax.set_yticklabels(coffee_varieties)
ax.set_xlabel('Months', labelpad=10)
ax.set_ylabel('Coffee Varieties', labelpad=10)
ax.set_zlabel('Units Sold', labelpad=10)

ax.view_init(elev=20, azim=135)
ax.set_title('Monthly Sales Performance\nand Average Sales of Coffee Varieties', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()