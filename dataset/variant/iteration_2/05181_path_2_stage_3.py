import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
avg_screen_sizes = np.array([3.5, 3.7, 4.0, 4.5, 4.7, 5.0, 5.2, 5.5, 5.7, 6.1, 6.4])

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(years, avg_screen_sizes, color='blue', marker='s', linestyle='--', linewidth=2, label='Avg Screen Size')

plt.title('Evolution of Smartphone Screen Sizes (2010 - 2020)', fontsize=18, fontweight='bold', color='purple', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Screen Size (inches)', fontsize=12)

ax.set_xticks(years)
ax.set_yticks(np.arange(3.0, 7.0, 0.5))
ax.grid(True, linestyle='-.', alpha=0.6)

ax.legend(loc='lower right', fontsize=10)

plt.tight_layout()
plt.show()