import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June']
regions = ['North', 'South', 'East']

north_sales = [15, 20, 25, 22, 30, 35]
south_sales = [10, 15, 12, 20, 25, 28]
east_sales = [18, 22, 27, 30, 35, 40]

total_sales = [sum(north_sales), sum(south_sales), sum(east_sales)]
sales_data = list(zip(regions, total_sales))
sorted_sales_data = sorted(sales_data, key=lambda x: x[1], reverse=True)

sorted_regions, sorted_totals = zip(*sorted_sales_data)

colors = ['#28A745', '#FF5733', '#007ACC']

fig, ax = plt.subplots(figsize=(10, 7))

bar_width = 0.5
index = np.arange(len(sorted_regions))

bars = ax.bar(index, sorted_totals, bar_width, color=colors[:len(sorted_regions)], tick_label=sorted_regions)

ax.set_title("Total Sales Data of Tech Gadgets Store by Region: First Half of the Year", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Regions", fontsize=14)
ax.set_ylabel("Total Sales (Thousands of Units)", fontsize=14)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width()/2, height), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom', fontsize=10)

plt.show()