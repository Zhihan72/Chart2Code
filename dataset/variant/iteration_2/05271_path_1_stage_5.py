import matplotlib.pyplot as plt
import numpy as np

company_a = [35, 38, 40, 42, 47, 50, 53, 55, 58, 60, 63, 66]
company_b = [45, 48, 50, 54, 57, 60, 62, 65, 68, 70, 72, 75]
company_x = [55, 60, 58, 62, 65, 68, 70, 72, 75, 78, 82, 85]
company_y = [40, 42, 45, 47, 50, 51, 53, 55, 58, 60, 62, 64]
company_z = [30, 35, 32, 37, 38, 40, 41, 43, 45, 47, 49, 50]
company_w = [25, 27, 29, 30, 32, 34, 36, 37, 38, 39, 40, 41]

avg_revenue = [(c1 + c2 + c3 + c4 + c5 + c6) / 6 for c1, c2, c3, c4, c5, c6 in zip(company_a, company_b, company_x, company_y, company_z, company_w)]
colors = ['#8A2BE2', '#7FFF00', '#32CD32', '#FF6347', '#FFD700', '#4682B4']

fig, ax = plt.subplots(figsize=(14, 9))
x_indexes = np.arange(12)  # No need for month labels, so using range(12)

for revenue, color in zip([company_a, company_b, company_x, company_y, company_z, company_w], colors):
    divergence = [rev - avg for rev, avg in zip(revenue, avg_revenue)]
    ax.barh(x_indexes, divergence, color=color, alpha=0.8)

# Removed title and labels
ax.set_yticks(x_indexes)
ax.set_yticklabels(['']*12)  # Remove month labels

plt.tight_layout()
plt.show()