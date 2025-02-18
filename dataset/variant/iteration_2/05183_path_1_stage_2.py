import matplotlib.pyplot as plt
import numpy as np

# Data
instruments = ['Guitars', 'Pianos', 'Violins', 'Drums', 'Flutes', 'Saxophones']
sales = [150, 80, 60, 90, 45, 70]  # Sales in thousands of units
growth_rates = [7, 5, 10, 3, 8, 6]  # Year-over-year growth rates in percentage

fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for sales (Horizontal)
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
bars = ax1.barh(instruments, sales, color=bar_colors, edgecolor='black', label='Sales (Thousands)')
ax1.set_ylabel('Musical Instruments', fontsize=12)
ax1.set_xlabel('Sales (Thousands of Units)', fontsize=12, color='black')
ax1.set_title('Annual Sales of Musical Instruments (2022) and Yearly Growth Rates', fontsize=16, fontweight='bold')
ax1.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate bar lengths
for bar in bars:
    width = bar.get_width()
    ax1.annotate(f'{width}k', xy=(width, bar.get_y() + bar.get_height() / 2),
                 xytext=(3, 0), textcoords="offset points", ha='left', va='center', fontsize=10)

# Create a secondary axis for growth rates
ax2 = ax1.twiny()
ax2.plot(growth_rates, instruments, color='navy', marker='o', linestyle='-', linewidth=2, label='Growth Rate (%)')
ax2.set_xlabel('Growth Rate (%)', fontsize=12, color='navy')

# Annotate growth rates
for i, rate in enumerate(growth_rates):
    ax2.annotate(f'{rate}%', xy=(rate, i),
                 xytext=(5, 0), textcoords="offset points", ha='left', va='center', fontsize=10, color='navy')

# Create a legend for the line plot
lines, labels = ax2.get_legend_handles_labels()
ax2.legend(lines, labels, loc='lower right', fontsize=10)

# Tighten the layout and show the plot
fig.tight_layout()
plt.show()