import matplotlib.pyplot as plt
import numpy as np

countries = ['Latteville', 'Espressonia', 'Brewland', 'Mocha Town', 'Cappuccinia']
coffee_consumption = [10, 5, 8, 7, 11]  
economic_impact = [5.2, 2.1, 4.5, 3.1, 6.0]  

x_pos = np.arange(len(countries))
width = 0.35

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle('Caffeine Culture: Impact & Consumption', fontsize=18, fontweight='bold', y=0.98)

bars1 = ax1.bar(x_pos - width/2, coffee_consumption, width, color='#8B4513', edgecolor='black', linewidth=1.2, label='Annual (kg/person)')

bars2 = ax2.bar(x_pos + width/2, economic_impact, width, color='#D2691E', edgecolor='black', linewidth=1.2, label='Revenue (Bn USD)')

for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval} kg', ha='center', va='bottom', fontsize=10)

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval} B', ha='center', va='bottom', fontsize=10)

ax1.set_title('Per Capita Coffee Usage', fontsize=14, fontweight='bold', pad=10)
ax1.set_xlabel('Nations', fontsize=12)
ax1.set_ylabel('Usage (kg per person)', fontsize=12)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(countries, fontsize=11, rotation=30, ha='right')
ax1.set_ylim(0, 12)

ax2.set_title('Financial Footprint of Coffee', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('Nations', fontsize=12)
ax2.set_ylabel('Financial Gain (Billion USD)', fontsize=12)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(countries, fontsize=11, rotation=30, ha='right')
ax2.set_ylim(0, 7)

ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper left', fontsize=10)

plt.tight_layout(pad=2.0, rect=[0, 0.03, 1, 0.95])

plt.show()