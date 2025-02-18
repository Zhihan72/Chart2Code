import matplotlib.pyplot as plt
import numpy as np

categories = ["Apples", "Bananas", "Oranges", "Plums"]
q1_sales = [120, 80, 150, 60]
q2_sales = [130, 85, 160, 70]
q3_sales = [140, 95, 170, 75]
q4_sales = [150, 100, 180, 80]
avg_sales_per_quarter = np.mean([q1_sales, q2_sales, q3_sales, q4_sales], axis=0)

fig, ax1 = plt.subplots(figsize=(14, 8))
width = 0.2
x = np.arange(len(categories))

ax1.bar(x - 1.5*width, q1_sales, width, color='dodgerblue')
ax1.bar(x - 0.5*width, q2_sales, width, color='goldenrod')
ax1.bar(x + 0.5*width, q3_sales, width, color='seagreen')
ax1.bar(x + 1.5*width, q4_sales, width, color='tomato')

ax1.set_xticks([])
ax1.tick_params(axis='y', labelleft=False)

ax2 = ax1.twinx()
ax2.plot(categories, avg_sales_per_quarter, color='purple', linestyle='--', marker='o', markersize=8, alpha=0.7)
ax2.tick_params(axis='y', labelright=False)

plt.show()