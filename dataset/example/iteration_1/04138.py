import matplotlib.pyplot as plt
import numpy as np

# Define the data for the chart
years = np.arange(2000, 2024)
traditional_books_sales = [820, 810, 800, 780, 770, 760, 750, 740, 730, 720, 700, 680, 660, 640, 600, 560, 520, 480, 440, 400, 380, 360, 350, 340]
e_books_sales = [0, 10, 20, 50, 80, 120, 180, 220, 270, 320, 370, 420, 460, 500, 540, 580, 600, 620, 640, 660, 680, 690, 700, 710]
audiobooks_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 20, 30, 50, 70, 90, 110, 130, 150, 180, 220, 270, 330]

# Stack the data
sales_data = np.vstack([traditional_books_sales, e_books_sales, audiobooks_sales])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
ax.stackplot(years, sales_data, labels=['Traditional Books', 'E-books', 'Audiobooks'], 
             colors=colors, alpha=0.9)

# Create detailed title and labels
plt.title('Evolution of Book Sales Formats\n(2000-2023)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14, labelpad=10)
plt.ylabel('Sales (in 1000 units)', fontsize=14, labelpad=10)

# Customize ticks and grid
plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(0, 901, 100))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend
plt.legend(loc='upper left', fontsize=12, frameon=False)

# Add annotations to highlight trends
ax.annotate('Rise of E-books', xy=(2012, 200), xytext=(2005, 450),
            bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='orange', ha='center')

ax.annotate('Growth of Audiobooks', xy=(2020, 330), xytext=(2013, 500),
            bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='green', ha='center')

# Adjust layout for better visualization
plt.tight_layout()

# Create an inset plot for the growth of audiobooks
left, bottom, width, height = [0.6, 0.5, 0.3, 0.3]
ax_inset = fig.add_axes([left, bottom, width, height])
ax_inset.plot(years, audiobooks_sales, marker='o', color='#2ca02c', linestyle='-')
ax_inset.set_title('Audiobooks Growth', fontsize=10)
ax_inset.set_xlabel('Year', fontsize=8)
ax_inset.set_ylabel('Sales (in 1000 units)', fontsize=8)
ax_inset.tick_params(axis='both', which='major', labelsize=8)

# Show plot
plt.show()