import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2018', '2019', '2020', '2021', '2022'])
fruits = ["Apples", "Bananas", "Oranges", "Grapes", "Strawberries"]

apples_sales = np.array([275, 250, 320, 300, 310])
bananas_sales = np.array([220, 240, 230, 180, 210])
oranges_sales = np.array([210, 240, 200, 190, 220])
grapes_sales = np.array([170, 180, 150, 160, 175])
strawberries_sales = np.array([130, 120, 115, 90, 110])

colors = ['#581845', '#DAF7A6', '#C70039', '#FFC300', '#FF5733']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
x = np.arange(len(years))

for i, fruit in enumerate(fruits):
    ax.bar(x + i*bar_width, eval(f"{fruit.lower()}_sales"), width=bar_width, label=fruit, color=colors[i])

ax.set_title("Annual Fruit Sales Analysis (2018-2022)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Sales (in tons)", fontsize=12)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years, fontsize=12)
ax.legend(title='Fruits', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()