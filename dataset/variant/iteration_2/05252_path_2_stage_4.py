import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

city_a = np.array([80, 75, 70, 60, 65, 55, 90, 85, 75, 95, 100, 80])
city_b = np.array([95, 85, 80, 75, 65, 105, 100, 90, 110, 90, 95, 75])
city_c = np.array([60, 70, 55, 45, 50, 65, 75, 50, 60, 70, 55, 65])

data = np.vstack([city_a, city_b, city_c])

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(months, data, labels=['City A', 'City B', 'City C'],
             colors=['#e15759', '#76b7b2', '#59a14f'], alpha=0.7)

ax.set_title("2021 City Rainfall", fontsize=17, fontweight='bold', pad=25)
ax.set_xlabel("Month", fontsize=11, weight='bold')
ax.set_ylabel("Rain/mm", fontsize=11, weight='bold')
ax.legend(loc='upper left', frameon=False, fontsize=9, title='City Names', title_fontsize='11')
ax.grid(True, which='both', linestyle='-.', linewidth=0.6, alpha=0.6)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)} mm'))
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, fontsize=9, rotation=40)
ax.set_yticks(np.arange(0, 301, 60))
ax.set_yticklabels(np.arange(0, 301, 60), fontsize=9)

plt.tight_layout()
plt.show()