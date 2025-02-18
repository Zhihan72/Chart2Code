import matplotlib.pyplot as plt

energy_sources = ['Hydroelectric', 'Natural Gas', 'Solar', 'Coal', 'Wind', 'Nuclear']
carbon_emissions = [43, 16, 24, 490, 820, 10]  # Manually shuffled
cost = [40, 50, 65, 50, 112, 30]  # Manually shuffled
capacity = [800, 450, 1000, 300, 400, 500]  # Manually shuffled

fig, ax1 = plt.subplots(figsize=(14, 8))

single_color = 'tab:purple'
ax1.set_xlabel('Power Type')
ax1.set_ylabel('Emissions (gCO2/kWh)', color=single_color)
ax1.bar(energy_sources, carbon_emissions, color=single_color, alpha=0.6, label='Emissions')
ax1.tick_params(axis='y', labelcolor=single_color)

ax2 = ax1.twinx()
ax2.set_ylabel('Expense ($/MWh)', color=single_color)
ax2.bar(energy_sources, cost, color=single_color, alpha=0.6, width=0.4, align='edge')
ax2.tick_params(axis='y', labelcolor=single_color)

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel('Output (MW)', color=single_color)
ax3.bar(energy_sources, capacity, color=single_color, alpha=0.6, width=0.4, align='center')
ax3.tick_params(axis='y', labelcolor=single_color)

plt.title('Environmental and Economic Profile of Power Types', fontsize=16, fontweight='bold', pad=20)
fig.tight_layout()

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.show()