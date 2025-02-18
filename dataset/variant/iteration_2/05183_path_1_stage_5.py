import matplotlib.pyplot as plt

instruments = ['Guitar', 'Piano', 'Violin', 'Drum', 'Flute', 'Sax']
sales = [150, 80, 60, 90, 45, 70]
growth_rates = [7, 5, 10, 3, 8, 6]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a6', '#ff8c33', '#8c33ff']
bars = ax1.barh(instruments, sales, color=bar_colors, edgecolor='#444', label='Sales (Thousands)', linewidth=1.5)
ax1.set_ylabel('Instruments', fontsize=13)
ax1.set_xlabel('Sales (k Units)', fontsize=11, color='navy')
ax1.set_title('2022 Sales & Growth', fontsize=17, fontweight='bold')
ax1.xaxis.grid(True, linestyle='-.', linewidth=0.7, alpha=0.5)

for bar in bars:
    width = bar.get_width()
    ax1.annotate(f'{width}k', xy=(width, bar.get_y() + bar.get_height() / 2),
                 xytext=(3, 0), textcoords="offset points", ha='left', va='center', fontsize=10)

ax2 = ax1.twiny()
ax2.plot(growth_rates, instruments, color='darkred', marker='s', linestyle='--', linewidth=2.5, label='Growth (%)')
ax2.set_xlabel('Growth (%)', fontsize=12, color='darkred')

for i, rate in enumerate(growth_rates):
    ax2.annotate(f'{rate}%', xy=(rate, i),
                 xytext=(5, 0), textcoords="offset points", ha='left', va='center', fontsize=10, color='darkred')

lines, labels = ax2.get_legend_handles_labels()
ax2.legend(lines, labels, loc='upper left', fontsize=10)

fig.tight_layout()
plt.show()