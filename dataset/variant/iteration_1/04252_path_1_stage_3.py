import matplotlib.pyplot as plt

energy_sources = ['Wind', 'Nuclear', 'Hydroelectric', 'Solar', 'Natural Gas', 'Coal']
carbon_emissions = [24, 10, 820, 43, 16, 490]  # Randomly shuffled
cost = [65, 30, 112, 40, 50, 50]  # Randomly shuffled
capacity = [1000, 500, 400, 800, 450, 300]  # Randomly shuffled

fig, ax1 = plt.subplots(figsize=(14, 8))

single_color = 'tab:purple'
ax1.set_xlabel('Energy Source')
ax1.set_ylabel('Carbon Emissions (gCO2/kWh)', color=single_color)
ax1.bar(energy_sources, carbon_emissions, color=single_color, alpha=0.6, label='Carbon Emissions')
ax1.tick_params(axis='y', labelcolor=single_color)

ax2 = ax1.twinx()
ax2.set_ylabel('Cost ($/MWh)', color=single_color)
ax2.bar(energy_sources, cost, color=single_color, alpha=0.6, width=0.4, align='edge')
ax2.tick_params(axis='y', labelcolor=single_color)

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel('Capacity (MW)', color=single_color)
ax3.bar(energy_sources, capacity, color=single_color, alpha=0.6, width=0.4, align='center')
ax3.tick_params(axis='y', labelcolor=single_color)

plt.title('Comparative Footprint of Various Energy Sources', fontsize=16, fontweight='bold', pad=20)
fig.tight_layout()

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.show()