import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

action_sales = np.array([45, 50, 47, 55, 60, 63, 65, 68, 75, 72, 80])
drama_sales = np.array([35, 37, 39, 42, 48, 50, 53, 55, 57, 60, 62])
scifi_sales = np.array([25, 28, 30, 33, 35, 36, 40, 44, 46, 49, 53])

fig, (ax2, ax1) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [1, 3]})

total_sales = action_sales + drama_sales + scifi_sales
ax2.plot(years, total_sales, marker='o', linestyle='-', color='brown', linewidth=2)
ax2.set_xlabel('Yr', fontsize=12)
ax2.set_ylabel('Total Sales (M)', fontsize=12)

# Shuffling the assigned colors
ax1.plot(years, action_sales, marker='o', linestyle='-', color='green', linewidth=2)
ax1.plot(years, drama_sales, marker='o', linestyle='-', color='purple', linewidth=2)
ax1.plot(years, scifi_sales, marker='o', linestyle='-', color='red', linewidth=2)

annotations = {
    'Act': (years[np.argmax(action_sales)], max(action_sales)),
    'Dra': (years[np.argmax(drama_sales)], max(drama_sales)),
    'SF': (years[np.argmax(scifi_sales)], max(scifi_sales))
}

for genre, (year, value) in annotations.items():
    ax1.annotate(f'{value}', xy=(year, value), xytext=(year + 0.3, value),
                 arrowprops=dict(facecolor='black', arrowstyle="->"))

ax1.set_xlabel('Yr', fontsize=12)
ax1.set_ylabel('Sales (M)', fontsize=12)

fig.suptitle('Ticket Sales (2010-2020)', fontsize=16, fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()