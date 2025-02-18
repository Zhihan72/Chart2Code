import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
companies = ['Company X', 'Company Y', 'Company Z', 'Company W']

company_x = [55, 60, 58, 62, 65, 68, 70, 72, 75, 78, 82, 85]
company_y = [40, 42, 45, 47, 50, 51, 53, 55, 58, 60, 62, 64]
company_z = [30, 35, 32, 37, 38, 40, 41, 43, 45, 47, 49, 50]
company_w = [25, 27, 29, 30, 32, 34, 36, 37, 38, 39, 40, 41]

avg_revenue = [(c1 + c2 + c3 + c4) / 4 for c1, c2, c3, c4 in zip(company_x, company_y, company_z, company_w)]

# Reordered colors for each company
colors = ['#32CD32', '#FF6347', '#FFD700', '#4682B4']

fig, ax = plt.subplots(figsize=(14, 9))
x_indexes = np.arange(len(months))

for revenue, company, color in zip([company_x, company_y, company_z, company_w], companies, colors):
    divergence = [rev - avg for rev, avg in zip(revenue, avg_revenue)]
    ax.barh(x_indexes, divergence, label=company, color=color, alpha=0.8)

ax.set_title('Diverging Monthly Revenue Contributions in 2022', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Revenue Divergence (in thousands of dollars)', fontsize=14)
ax.set_yticks(x_indexes)
ax.set_yticklabels(months)

ax.legend(title='Subsidiary Companies', loc='upper right', fontsize=12, title_fontsize='13')

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()