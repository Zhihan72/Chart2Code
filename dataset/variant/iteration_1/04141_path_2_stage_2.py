import matplotlib.pyplot as plt
import numpy as np

# Data parameters
product_lines = [
    'Smartphones', 'Laptops', 'Accessories',
    'Services', 'Software', 'Wearables', 'AI Solutions'
]
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Revenue data
revenue_data = [
    [45.6, 48.2, 50.1, 52.3],
    [30.8, 33.6, 35.2, 37.8],
    [10.5, 12.0, 11.8, 13.2],
    [14.0, 15.8, 16.5, 17.9],
    [20.1, 21.5, 22.4, 23.9],
    [9.2, 10.3, 10.9, 12.0],
    [18.4, 19.6, 20.2, 21.5]
]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A4', '#FFC133', '#33FFF6', '#F633FF']

# Calculate total revenue for sorting
total_revenue = [sum(revenue) for revenue in revenue_data]

# Sort by total revenue
sorted_indices = np.argsort(total_revenue)
sorted_product_lines = [product_lines[i] for i in sorted_indices]
sorted_revenue_data = [revenue_data[i] for i in sorted_indices]
sorted_colors = [colors[i] for i in sorted_indices]
sorted_total_revenue = sorted(total_revenue)

# Create the sorted bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
bar_width = 0.1
bar_positions = np.arange(len(quarters))

# Plot revenue for each product line (sorted)
for i, product in enumerate(sorted_product_lines):
    ax1.bar(bar_positions + i * bar_width, sorted_revenue_data[i], color=sorted_colors[i], width=bar_width, edgecolor='grey', label=product)

# Add titles and labels
ax1.set_title('TechyGears Quarterly Revenue Analysis for 2023', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Quarters', fontsize=14)
ax1.set_ylabel('Revenue (in Millions USD)', fontsize=14)
ax1.set_xticks(bar_positions + (len(product_lines) - 1) * bar_width / 2)
ax1.set_xticklabels(quarters)

# Annotate each bar with the exact value
for i, product in enumerate(sorted_product_lines):
    for j, value in enumerate(sorted_revenue_data[i]):
        ax1.text(j + i * bar_width, value + 0.5, f"{value:.1f}", ha='center', va='bottom', fontsize=10, color='black')

# Enhance plot aesthetics
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_axisbelow(True)

# Plot total annual revenue for each product line (sorted)
ax2.barh(sorted_product_lines, sorted_total_revenue, color=sorted_colors, edgecolor='grey')

# Add titles and labels
ax2.set_title('Total Annual Revenue by Product Line - 2023', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Total Revenue (in Millions USD)', fontsize=14)
ax2.set_ylabel('Product Lines', fontsize=14)

# Annotate each bar with the exact value
for i, total in enumerate(sorted_total_revenue):
    ax2.text(total + 1, i, f"{total:.1f}", va='center', ha='left', fontsize=12, color='black')

# Adjust layout for better appearance
plt.tight_layout()

# Display the plot
plt.show()