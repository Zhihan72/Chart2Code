import matplotlib.pyplot as plt
import numpy as np

years = [2021, 2022, 2023]
genres = [
    'Fiction', 'Non-Fiction', 'Fantasy', 'Science Fiction', 
    'Mystery', 'Historical', 'Biography', 'Romance', 'Horror'
]
sales_data = {
    2021: [1400, 1100, 750, 950, 1050, 550, 300, 800, 400],
    2022: [1500, 1200, 800, 1000, 1100, 600, 400, 900, 500],
    2023: [1600, 1300, 850, 1050, 1150, 650, 500, 950, 600]
}

colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33C4', '#33FFC4', '#FFC300', '#C70039', '#900C3F']
fig, ax = plt.subplots(figsize=(14, 10))
width = 0.25
x = np.arange(len(genres))

for i, year in enumerate(years):
    sales = sales_data[year]
    ax.bar(x + i*width, sales, width=width, color=colors, edgecolor='black')

# Customize ticks without labels
ax.set_xticks(x + width)
ax.set_xticklabels([])

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.tight_layout()
plt.show()