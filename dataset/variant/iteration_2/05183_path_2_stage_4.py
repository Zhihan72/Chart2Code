import matplotlib.pyplot as plt
import numpy as np

instruments = ['Gtr', 'Drm', 'Pn', 'Flt']
sales = [150, 90, 80, 45]
growth_rates = [7, 3, 5, 8]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_colors = ['#1f77b4', '#ff7f0e', '#d62728', '#9467bd']

# Bar chart for sales
bars = ax1.bar(instruments, sales, color=bar_colors, edgecolor='gray')
ax1.set_xlabel('Instruments', fontsize=12)
ax1.set_ylabel('Sales (k Units)', fontsize=12, color='black')
ax1.set_title('2022 Sales & Growth', fontsize=16, fontweight='bold')
ax1.yaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.7)

# Annotate bar heights
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}k', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

# Create a secondary axis for growth rates
ax2 = ax1.twinx()
ax2.plot(instruments, growth_rates, color='navy', marker='^', linestyle='--', linewidth=2, label='Growth (%)')
ax2.set_ylabel('Growth (%)', fontsize=12, color='navy')

# Annotate growth rates
for i, rate in enumerate(growth_rates):
    ax2.annotate(f'{rate}%', xy=(i, rate),
                 xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='navy')

# Create a legend for the line plot
lines, labels = ax2.get_legend_handles_labels()
ax2.legend(lines, labels, loc='upper right', fontsize=10)

fig.tight_layout()
plt.show()