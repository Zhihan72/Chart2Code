import matplotlib.pyplot as plt
import numpy as np

# Manually shuffled transport modes
transport_modes = ['Autonomous Buses', 'Flying Cars', 'Hyperloop', 'Teleports', 'MagLev Trains']
# Corresponding adoption rates adjusted to match shuffled transport modes
adoption_rates = np.array([90, 120, 80, 60, 150])
# Manually shuffled colors matching the new order of transport modes
colors = ['#33ffa8', '#ff5733', '#ff33a8', '#33ff57', '#3357ff']

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(np.arange(len(transport_modes)), adoption_rates, color=colors, edgecolor='grey', linewidth=2, height=0.55, linestyle='-.')

ax.set_title('2050 Yearly Rates of Adopted Transports', fontsize=18, fontweight='heavy', pad=25)
ax.set_xlabel('Thousands of Adoption Rate', fontsize=12, fontstyle='italic', color='darkblue')
ax.set_ylabel('Future Transport Enablers', fontsize=12, fontstyle='italic', color='darkred')

ax.set_yticks(np.arange(len(transport_modes)))
ax.set_yticklabels(transport_modes, fontsize=10)

for bar in bars:
    xval = bar.get_width()
    ax.text(xval + 3, bar.get_y() + bar.get_height()/2, f'{xval}k', ha='left', va='center', fontsize=10, fontweight='medium')

# Manually shuffled legend labels to match the new order of transport modes
legend_labels = ['Fast', 'Instant', 'Rapid', 'Luxurious', 'Eco']
ax.legend(bars, legend_labels, title='Characteristics', title_fontsize='10', loc='best', fontsize=8, frameon=True, shadow=True, fancybox=True)

plt.tight_layout()
plt.show()