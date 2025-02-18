import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

city_a = np.array([80, 70, 75, 60, 55, 65, 85, 90, 70, 80, 95, 100])
city_b = np.array([90, 80, 85, 75, 65, 75, 95, 100, 90, 95, 110, 105])
city_c = np.array([60, 55, 50, 45, 50, 55, 65, 70, 60, 65, 70, 75])
city_d = np.array([50, 45, 55, 50, 60, 70, 80, 85, 75, 80, 85, 90])
city_e = np.array([100, 95, 105, 95, 80, 85, 90, 95, 110, 115, 120, 125])

data = np.vstack([city_a, city_b, city_c, city_d, city_e])

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(months, data, labels=['A', 'B', 'C', 'D', 'E'],
             colors=['#184c83', '#df6b31', '#299c4a', '#a92320', '#6f579b'], alpha=0.8)

ax.set_title("Monthly Rainfall\nfor Cities", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Mon", fontsize=12, weight='bold')
ax.set_ylabel("Rain (mm)", fontsize=12, weight='bold')
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10, title='Cties')
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, fontsize=10, rotation=45)
ax.set_yticks(np.arange(0, 501, 50))
ax.set_yticklabels(np.arange(0, 501, 50), fontsize=10)

plt.tight_layout()

plt.show()