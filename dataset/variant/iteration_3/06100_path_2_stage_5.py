import matplotlib.pyplot as plt
import numpy as np

north_sales = [15, 20, 25, 22, 30, 35]
south_sales = [10, 15, 12, 20, 25, 28]
east_sales = [18, 22, 27, 30, 35, 40]

total_sales = [sum(north_sales), sum(south_sales), sum(east_sales)]
sales_data = list(zip(['North', 'South', 'East'], total_sales))
sorted_sales_data = sorted(sales_data, key=lambda x: x[1], reverse=True)

sorted_regions, sorted_totals = zip(*sorted_sales_data)

# Applying a single color across all bars
single_color = '#007ACC'

fig, ax = plt.subplots(figsize=(10, 7))

bar_width = 0.5
index = np.arange(len(sorted_regions))

bars = ax.bar(index, sorted_totals, bar_width, color=single_color, tick_label=sorted_regions)

ax.set_title("Altered Total Gadget Sales Genre-wise: Mid-year Analysis", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Districts", fontsize=14)
ax.set_ylabel("Cumulative Units Sold (K)", fontsize=14)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'Volume: {height}', xy=(bar.get_x() + bar.get_width()/2, height), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom', fontsize=10)

plt.show()