import matplotlib.pyplot as plt
import numpy as np

# Define book genres and monthly sales data (Removed 'Horror')
genres = ['Mystery', 'Romance', 'Science Fiction', 'Fantasy', 'Non-fiction']
monthly_sales = np.array([
    [120, 130, 140, 150, 160, 170],  # Mystery
    [200, 190, 220, 210, 230, 240],  # Romance
    [180, 175, 190, 185, 195, 200],  # Science Fiction
    [160, 170, 180, 190, 200, 210],  # Fantasy
    [220, 210, 230, 220, 240, 250]   # Non-fiction
])

# Aggregate yearly sales
yearly_sales = monthly_sales.sum(axis=1)

# Define months for x-axis of subplots
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Colors for the bar charts
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(genres)))

# Create the figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plotting the monthly sales data as a grouped bar chart
width = 0.15  # width of bars
x = np.arange(len(months))  # label locations

for i in range(len(genres)):
    ax1.bar(x + i * width, monthly_sales[i], width, label=genres[i], color=colors[i], edgecolor='black')

# Setting title and labels for the grouped bar chart subplot
ax1.set_title('Monthly Book Sales by Genre\n(Jan-Jun)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Number of Books Sold', fontsize=14)
ax1.set_xticks(x + width * (len(genres) - 1) / 2)
ax1.set_xticklabels(months, fontsize=12)
ax1.legend(title='Genres', fontsize=10)

# Plotting the yearly sales data as a bar chart
bars = ax2.barh(genres, yearly_sales, color=colors, edgecolor='black')

# Setting title and labels for the yearly sales bar chart subplot
ax2.set_title('Total Yearly Sales by Genre', fontsize=16, fontweight='bold')
ax2.set_xlabel('Number of Books Sold', fontsize=14)
ax2.set_ylabel('Genre', fontsize=14)

# Annotate bars with the total count
for bar in bars:
    width = bar.get_width()
    ax2.text(width + 5, bar.get_y() + bar.get_height() / 2, f'{int(width)}', 
             va='center', fontsize=10, color='black', weight='bold')

# Add grid to the y-axis
ax2.xaxis.grid(True, linestyle='--', alpha=0.6)
ax2.set_axisbelow(True)

# Adjust layout to prevent text from overlapping and ensure neat presentation
plt.tight_layout()

# Display the plot
plt.show()