import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

action_sales = np.array([45, 50, 47, 55, 60, 63, 65, 68, 75, 72, 80])
comedy_sales = np.array([40, 42, 41, 45, 50, 52, 49, 54, 59, 58, 60])
drama_sales = np.array([35, 37, 39, 42, 48, 50, 53, 55, 57, 60, 62])
scifi_sales = np.array([25, 28, 30, 33, 35, 36, 40, 44, 46, 49, 53])
horror_sales = np.array([30, 32, 35, 38, 40, 43, 47, 50, 53, 56, 58])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [3, 1]})

total_sales = action_sales + comedy_sales + drama_sales + scifi_sales + horror_sales
ax1.plot(years, total_sales, marker='x', linestyle='-', color='black', linewidth=2.5)
ax1.grid(axis='both', linestyle=':', alpha=0.5)

ax2.plot(years, action_sales, marker='s', linestyle='--', color='purple', linewidth=2.5)
ax2.plot(years, comedy_sales, marker='^', linestyle='-.', color='darkgreen', linewidth=2.5)
ax2.plot(years, drama_sales, marker='D', linestyle=':', color='navy', linewidth=2.5)
ax2.plot(years, scifi_sales, marker='*', linestyle='-', color='coral', linewidth=2.5)
ax2.plot(years, horror_sales, marker='o', linestyle='-', color='grey', linewidth=2.5)

annotations = {
    'Action': (years[np.argmax(action_sales)], max(action_sales)),
    'Comedy': (years[np.argmax(comedy_sales)], max(comedy_sales)),
    'Drama': (years[np.argmax(drama_sales)], max(drama_sales)),
    'Sci-Fi': (years[np.argmax(scifi_sales)], max(scifi_sales)),
    'Horror': (years[np.argmax(horror_sales)], max(horror_sales))
}

for genre, (year, value) in annotations.items():
    ax2.annotate(f'{value}', xy=(year, value), xytext=(year + 0.5, value + 3),
                 arrowprops=dict(facecolor='red', linestyle='-', arrowstyle="->"))

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()