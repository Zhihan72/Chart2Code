import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

apple_sales = [18, 15, 24, 20, 27, 30, 34, 38, 45, 42, 50]
orange_sales = [12, 10, 15, 14, 20, 17, 25, 22, 29, 27, 32]
banana_sales = [9, 8, 11, 10, 17, 14, 24, 21, 30, 27, 34]

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(years, apple_sales, marker='o', linestyle='-', color='yellow', linewidth=2, markersize=6)
ax.plot(years, orange_sales, marker='s', linestyle='--', color='r', linewidth=2, markersize=6)
ax.plot(years, banana_sales, marker='^', linestyle='-.', color='orange', linewidth=2, markersize=6)

for year, sales in zip(years, apple_sales):
    ax.annotate(f'{sales}K', xy=(year, sales), xytext=(0, 8), textcoords='offset points', fontsize=9, ha='center', color='darkgoldenrod')

for year, sales in zip(years, orange_sales):
    ax.annotate(f'{sales}K', xy=(year, sales), xytext=(0, 8), textcoords='offset points', fontsize=9, ha='center', color='darkred')

for year, sales in zip(years, banana_sales):
    ax.annotate(f'{sales}K', xy=(year, sales), xytext=(0, 8), textcoords='offset points', fontsize=9, ha='center', color='darkorange')

ax.set_title('Fruit Evolution Over Decade', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Volume (K Units)', fontsize=14)

plt.tight_layout()
plt.show()