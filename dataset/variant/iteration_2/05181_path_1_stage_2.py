import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
avg_screen_sizes = np.array([3.5, 3.7, 4.0, 4.5, 4.7, 5.0, 5.2, 5.5, 5.7, 6.1, 6.4])
notable_models = {"iPhone 4": (2010, 3.5), "Samsung S3": (2012, 4.8), 
                  "iPhone 6": (2014, 4.7), "Samsung S8": (2017, 5.8), "iPhone 11": (2019, 6.1)}

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, avg_screen_sizes, color='green', marker='s', linestyle='--', linewidth=3, label='Avg Screen Size')

for model, (year, size) in notable_models.items():
    ax.plot(year, size, color='blue', marker='D')
    ax.text(year, size + 0.1, model, color='blue', ha='center', fontsize=10)

plt.title('Evolution of Smartphone Screen Sizes (2010 - 2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Screen Size (inches)', fontsize=12)

ax.set_xticks(years)
ax.set_yticks(np.arange(3.0, 7.0, 0.5))

ax.grid(True, linestyle='-', alpha=0.9)

ax.legend(loc='lower right', fontsize=10)

plt.tight_layout()

plt.show()