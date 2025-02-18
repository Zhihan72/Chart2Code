import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
age_groups = ['10-19', '20-29', '30-39', '40-49', '50+']
books_read = [5, 7, 8, 9, 12]
variability = [1, 1.5, 1.2, 1.3, 1.8]

# Data for the pie chart:
genre_distribution = [30, 25, 20, 15, 10]

# Colors for the bar chart and pie chart
bar_colors = ['#4CAF50', '#FFC107', '#2196F3', '#FF5722', '#9C27B0']
pie_colors = ['#ffe0b3', '#ffcc99', '#ffebcc', '#ccffe6', '#ccf2ff']

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Horizontal bar chart
ax1.barh(age_groups, books_read, color=bar_colors, edgecolor='black', 
         height=0.6, xerr=variability, capsize=5)
ax1.tick_params(axis='y', labelsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)

# Pie chart for genre preferences
ax2.pie(genre_distribution, startangle=90, colors=pie_colors, wedgeprops={'edgecolor': 'black'})

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(wspace=0.4)

# Show the plot
plt.show()