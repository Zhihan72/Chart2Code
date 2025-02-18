import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

company_x = [70, 62, 55, 78, 82, 65, 85, 58, 68, 72, 60, 75]
company_y = [50, 42, 64, 47, 62, 51, 40, 58, 45, 53, 55, 60]
company_z = [32, 37, 45, 50, 38, 40, 30, 35, 41, 49, 43, 32]
company_w = [40, 39, 27, 25, 34, 41, 36, 38, 29, 30, 37, 32]

revenue_data = [company_x, company_y, company_z, company_w]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

fig, ax = plt.subplots(figsize=(14, 9))

bar_width = 0.7
x_indexes = np.arange(len(months))

bottom = np.zeros(len(months))
for i, revenue in enumerate(revenue_data):
    ax.bar(x_indexes, revenue, width=bar_width, color=colors[i], bottom=bottom)
    bottom += np.array(revenue)

ax.set_title('Monthly Revenue Contributions from Subsidiary Companies in 2022\nCompany ABC Financial Overview', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Revenue (in thousands of dollars)', fontsize=14)

plt.xticks(ticks=x_indexes, labels=months, rotation=45, ha='right')
plt.yticks(np.arange(0, 300, 20))

plt.tight_layout()
plt.show()