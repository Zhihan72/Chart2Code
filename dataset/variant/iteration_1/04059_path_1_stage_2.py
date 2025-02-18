import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Data
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Romance', 'Mystery', 'Biography']
average_annual_sales = np.array([8000, 6000, 3000, 5000, 4500, 2000])
total_sales = np.sum(average_annual_sales)
percentage_sales = (average_annual_sales / total_sales) * 100

# New set of colors for genres
new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#0082c8', '#f58231', '#911eb4']

# Create a figure with bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Bar Chart
bars = ax.bar(genres, average_annual_sales, color=new_colors, edgecolor='black')

# Title and Labels
ax.set_title('Library Book Sales Analysis (2011-2021)', fontsize=16, fontweight='bold')
ax.set_xlabel('Book Genres', fontsize=12)
ax.set_ylabel('Average Annual Sales', fontsize=12)

# Display sales values on top of the bars
for bar, sales in zip(bars, average_annual_sales):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{sales}', 
            ha='center', va='bottom', fontsize=10, color='black')

# Inset Donut Chart
ax_inset = inset_axes(ax, width="40%", height="40%", loc="upper right")

# Donut Chart
ax_inset.pie(percentage_sales, labels=genres, autopct='%1.1f%%', startangle=140, colors=new_colors, pctdistance=0.85,
             wedgeprops=dict(width=0.3, edgecolor='w'), textprops={'color': 'black', 'fontsize': 8})

# Center text
ax_inset.text(0, 0, 'Genre \nDistribution', 
              horizontalalignment='center', verticalalignment='center', 
              fontsize=12, fontweight='bold')

# Remove axes from pie chart
ax_inset.axis('off')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()