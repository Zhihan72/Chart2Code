import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2018', '2019', '2020', '2021', '2022'])
fruits = ["Green Apples", "Yellow Bananas", "Citrus Oranges", "Purple Grapes", "Delight Strawberries"]

apples_sales = np.array([275, 250, 320, 300, 310])
bananas_sales = np.array([220, 240, 230, 180, 210])
oranges_sales = np.array([210, 240, 200, 190, 220])
grapes_sales = np.array([170, 180, 150, 160, 175])
strawberries_sales = np.array([130, 120, 115, 90, 110])

colors = ['#581845', '#DAF7A6', '#C70039', '#FFC300', '#FF5733']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
x = np.arange(len(years))

# Plotting bars without labels
for i, fruit in enumerate(fruits):
    ax.bar(x + i * bar_width, eval(f"{fruit.split()[1].lower()}_sales"), width=bar_width, color=colors[i])

# Set the title and labels
ax.set_title("Fruit Sale Trends and Nuances", fontsize=16, fontweight='bold')
ax.set_xlabel("Chronological Year", fontsize=12)
ax.set_ylabel("Volume Sold (tons)", fontsize=12)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years, fontsize=12)

# Removed grid and legend
plt.tight_layout()
plt.show()