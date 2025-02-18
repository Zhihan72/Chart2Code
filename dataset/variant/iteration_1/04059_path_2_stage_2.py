import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Data
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Romance', 'Mystery', 'Biography']
average_annual_sales = np.array([4500, 8000, 2000, 6000, 3000, 5000])  
total_sales = np.sum(average_annual_sales)
percentage_sales = (average_annual_sales / total_sales) * 100

# Colors for genres
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0', '#ffb3e6']

# Create a figure with a subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Bar Chart
bars = ax.bar(genres, average_annual_sales, color=colors, edgecolor='black')

# Title and Labels
ax.set_title('Library Book Sales Analysis (2011-2021)', fontsize=16, fontweight='bold')
ax.set_xlabel('Book Genres', fontsize=12)
ax.set_ylabel('Average Annual Sales', fontsize=12)

# Display the sales values on top of the bars
for bar, sales in zip(bars, average_annual_sales):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{sales}', 
            ha='center', va='bottom', fontsize=10, color='black')

# Inset Donut Chart
ax_inset = inset_axes(ax, width="40%", height="40%", loc="upper right")
ax_inset.pie(percentage_sales, labels=genres, autopct='%1.1f%%', startangle=140, colors=colors, pctdistance=0.85,
             wedgeprops=dict(width=0.3, edgecolor='w'), textprops={'color': 'black', 'fontsize': 8})

# Center text inside the donut
ax_inset.text(0, 0, 'Genre \nDistribution', 
              horizontalalignment='center', verticalalignment='center', 
              fontsize=12, fontweight='bold')

# Remove axes from the inset chart
ax_inset.axis('off')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()