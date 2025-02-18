import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart (after removing 'Violins')
instruments = ['Guitars', 'Pianos', 'Drums', 'Flutes']
sales = [150, 80, 90, 45]  # Sales in thousands of units

# Data for the line plot (after removing 'Violins')
growth_rates = [7, 5, 3, 8]  # Year-over-year growth rates in percentage

# Create the plot with one subplot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Colors for the bar chart, one color removed
bar_colors = ['#1f77b4', '#ff7f0e', '#d62728', '#9467bd']

# Bar chart for sales
bars = ax1.bar(instruments, sales, color=bar_colors, edgecolor='black', label='Sales (Thousands)')
ax1.set_xlabel('Musical Instruments', fontsize=12)
ax1.set_ylabel('Sales (Thousands of Units)', fontsize=12, color='black')
ax1.set_title('Annual Sales of Musical Instruments (2022) and Yearly Growth Rates', fontsize=16, fontweight='bold')
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate bar heights
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}k', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

# Create a secondary axis for growth rates
ax2 = ax1.twinx()
ax2.plot(instruments, growth_rates, color='navy', marker='o', linestyle='-', linewidth=2, label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='navy')

# Annotate growth rates
for i, rate in enumerate(growth_rates):
    ax2.annotate(f'{rate}%', xy=(i, rate),
                 xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='navy')

# Create a legend for the line plot
lines, labels = ax2.get_legend_handles_labels()
ax2.legend(lines, labels, loc='upper left', fontsize=10)

# Tighten the layout and show the plot
fig.tight_layout()
plt.show()