import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Romance', 'Mystery', 'Biography', 'Fantasy', 'History']
average_annual_sales = np.array([8000, 6000, 3000, 5000, 4500, 2000, 7000, 3500])
total_sales = np.sum(average_annual_sales)
percentage_sales = (average_annual_sales / total_sales) * 100

new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#0082c8', '#f58231', '#911eb4', '#46f0f0', '#fabebe']

fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.bar(genres, average_annual_sales, color=new_colors)

# Remove text annotations from bar chart
# Remove text annotations from donut chart
ax_inset = inset_axes(ax, width="40%", height="40%", loc="upper right")
ax_inset.pie(percentage_sales, startangle=140, colors=new_colors, wedgeprops=dict(width=0.3, edgecolor='w'))

ax_inset.axis('off')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()

plt.show()