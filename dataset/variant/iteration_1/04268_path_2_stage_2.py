import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

apple_sales = [15, 18, 20, 24, 27, 30, 34, 38, 42, 45, 50]
orange_sales = [10, 12, 14, 15, 17, 20, 22, 25, 27, 29, 32]
banana_sales = [8, 9, 10, 11, 14, 17, 21, 24, 27, 30, 34]

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

ax.set_title('Decade of Fruit Sales Growth (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Sales (Thousands of Units)', fontsize=14)

plt.tight_layout()
plt.show()