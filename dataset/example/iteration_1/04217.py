import matplotlib.pyplot as plt
import numpy as np

# Backstory: This plot shows the yearly sales figures for different types of technological gadgets in a mid-sized electronic store from 2015 to 2025. 
# The company wants to analyze sales trends for Mobile Phones, Tablets, Laptops, and Desktops.

# Years from 2015 to 2025
years = np.arange(2015, 2026)

# Sales data for different gadgets in number of units sold
mobile_phones = [250, 300, 350, 380, 450, 500, 520, 530, 600, 650, 700]
tablets = [120, 130, 135, 140, 160, 170, 175, 190, 200, 220, 230]
laptops = [80, 95, 100, 105, 110, 120, 125, 130, 140, 150, 160]
desktops = [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10]

# Creating the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the bar chart
bar_width = 0.2
years_shifted = np.arange(len(years))  # Adjusting the position of years in the x-axis

ax.bar(years_shifted - bar_width, mobile_phones, width=bar_width, label='Mobile Phones', color='#1f77b4', alpha=0.8)
ax.bar(years_shifted, tablets, width=bar_width, label='Tablets', color='#ff7f0e', alpha=0.8)
ax.bar(years_shifted + bar_width, laptops, width=bar_width, label='Laptops', color='#2ca02c', alpha=0.8)
ax.bar(years_shifted + 2 * bar_width, desktops, width=bar_width, label='Desktops', color='#d62728', alpha=0.8)

# Setting the title and labels
ax.set_title('Yearly Sales Figures for Different Types of Gadgets\n(Mid-sized Electronics Store, 2015-2025)', fontsize=14, fontweight='bold')
ax.set_ylabel('Units Sold', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_xticks(years_shifted)
ax.set_xticklabels(years)

# Adding the legend
ax.legend(title="Gadget Type", fontsize=10, loc='upper left')

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Annotating a significant rise in Mobile Phones sales
ax.annotate('Significant Increase in Mobile Sales', xy=(7, mobile_phones[7]), xytext=(3, 400),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Tight layout for neatness
plt.tight_layout()

# Display the plot
plt.show()