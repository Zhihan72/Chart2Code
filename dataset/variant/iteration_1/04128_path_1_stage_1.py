import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

action_sales = np.array([45, 50, 47, 55, 60, 63, 65, 68, 75, 72, 80])
comedy_sales = np.array([40, 42, 41, 45, 50, 52, 49, 54, 59, 58, 60])
drama_sales = np.array([35, 37, 39, 42, 48, 50, 53, 55, 57, 60, 62])
scifi_sales = np.array([25, 28, 30, 33, 35, 36, 40, 44, 46, 49, 53])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})

ax1.plot(years, action_sales, marker='o', linestyle='-', color='orange', label='Action', linewidth=2)
ax1.plot(years, comedy_sales, marker='o', linestyle='-', color='cyan', label='Comedy', linewidth=2)
ax1.plot(years, drama_sales, marker='o', linestyle='-', color='magenta', label='Drama', linewidth=2)
ax1.plot(years, scifi_sales, marker='o', linestyle='-', color='lime', label='Sci-Fi', linewidth=2)

annotations = {
    'Action': (years[np.argmax(action_sales)], max(action_sales)),
    'Comedy': (years[np.argmax(comedy_sales)], max(comedy_sales)),
    'Drama': (years[np.argmax(drama_sales)], max(drama_sales)),
    'Sci-Fi': (years[np.argmax(scifi_sales)], max(scifi_sales))
}

for genre, (year, value) in annotations.items():
    ax1.annotate(f'{value}', xy=(year, value), xytext=(year + 0.3, value),
                 arrowprops=dict(facecolor='black', arrowstyle="->"))

total_sales = action_sales + comedy_sales + drama_sales + scifi_sales
ax2.plot(years, total_sales, marker='o', linestyle='-', color='darkgrey', linewidth=2)
ax2.set_title('Total Ticket Sales for All Genres Combined', fontsize=13)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Total Ticket Sales (in millions)', fontsize=12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

fig.suptitle('Movie Ticket Sales Trends Over a Decade\n(2010-2020)', fontsize=16, fontweight='bold')
ax1.set_title('Ticket Sales Trend for Each Genre', fontsize=13)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Ticket Sales (in millions)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()