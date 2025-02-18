import numpy as np
import matplotlib.pyplot as plt

months = ['Jun', 'Jan', 'Apr', 'Mar', 'May', 'Feb']
coffee_varieties = ['Mocha', 'Espresso', 'Americano', 'Latte', 'Cappuccino']
sales_data = np.array([
    [240, 150, 180, 200, 250],
    [150, 240, 180, 270, 330],
    [210, 200, 230, 250, 270],
    [200, 180, 220, 230, 260],
    [220, 210, 250, 260, 320],
    [180, 220, 190, 230, 260]
])

average_sales = sales_data.mean(axis=1)

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#4B0082']
dx = dy = 0.7

for y, color in enumerate(colors):
    xs = np.arange(len(months))
    ys = sales_data[:, y]
    ax.bar3d(xs, y, np.zeros_like(xs), dx, dy, ys, color=color, alpha=0.9, label=coffee_varieties[y])

ax.plot(np.arange(len(months)), [-0.5] * len(months), average_sales, color='darkorange', marker='s', linestyle='--', linewidth=2.5, label='Average Sales')

ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=30)
ax.set_yticks(np.arange(len(coffee_varieties)))
ax.set_yticklabels(coffee_varieties)
ax.set_xlabel('Months', labelpad=10)
ax.set_ylabel('Coffee Types', labelpad=10)
ax.set_zlabel('Units Sold', labelpad=10)

ax.view_init(elev=30, azim=150)

ax.set_title('Monthly Sales Performance\nand Average Units Sold by Coffee Type', fontsize=14, fontweight='normal', pad=20)
ax.legend(loc='lower right', fontsize=10)

plt.tight_layout()
plt.show()