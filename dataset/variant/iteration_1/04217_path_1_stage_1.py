import matplotlib.pyplot as plt
import numpy as np

# Sales data for different gadgets in number of units sold
gadgets = {
    'Mobile Phones': [250, 300, 350, 380, 450, 500, 520, 530, 600, 650, 700],
    'Tablets': [120, 130, 135, 140, 160, 170, 175, 190, 200, 220, 230],
    'Laptops': [80, 95, 100, 105, 110, 120, 125, 130, 140, 150, 160],
    'Desktops': [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10]
}

# Calculate total sales per gadget type over the years
total_sales = {gadget: sum(sales) for gadget, sales in gadgets.items()}

# Sort gadgets based on total sales in descending order
sorted_gadgets = sorted(total_sales.items(), key=lambda x: x[1], reverse=True)

# Names and sales after sorting
gadget_names, sorted_sales = zip(*sorted_gadgets)

# Creating the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the sorted bar chart
bar_width = 0.6
range_gadgets = np.arange(len(gadget_names))

ax.bar(range_gadgets, sorted_sales, width=bar_width, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

# Setting the title and labels
ax.set_title('Total Sales for Different Types of Gadgets\n(Mid-sized Electronics Store, 2015-2025)', fontsize=14, fontweight='bold')
ax.set_ylabel('Total Units Sold', fontsize=12)
ax.set_xlabel('Gadget Type', fontsize=12)
ax.set_xticks(range_gadgets)
ax.set_xticklabels(gadget_names)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Tight layout for neatness
plt.tight_layout()

# Display the plot
plt.show()