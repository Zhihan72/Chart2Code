import matplotlib.pyplot as plt

energy_sources = ['Hydroelectric', 'Natural Gas', 'Solar', 'Coal', 'Wind', 'Nuclear']
carbon_emissions = [43, 16, 24, 490, 820, 10]  # Manually shuffled
cost = [40, 50, 65, 50, 112, 30]  # Manually shuffled
capacity = [800, 450, 1000, 300, 400, 500]  # Manually shuffled

fig, ax1 = plt.subplots(figsize=(14, 8))

multi_color = ['tab:blue', 'tab:green', 'tab:red', 'tab:orange', 'tab:pink', 'tab:brown']
ax1.set_xlabel('Power Type')
ax1.set_ylabel('Emissions (gCO2/kWh)', color='tab:blue')
ax1.bar(energy_sources, carbon_emissions, color=multi_color, alpha=0.8, hatch='/')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.grid(True, linestyle='--', linewidth=0.5)

ax2 = ax1.twinx()
ax2.set_ylabel('Expense ($/MWh)', color='tab:green')
ax2.plot(energy_sources, cost, color='tab:green', linestyle=':', marker='o', linewidth=3)
ax2.tick_params(axis='y', labelcolor='tab:green')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 70))
ax3.set_ylabel('Output (MW)', color='tab:red')
ax3.scatter(energy_sources, capacity, color='tab:red', marker='s')
ax3.tick_params(axis='y', labelcolor='tab:red')

plt.title('Environmental and Economic Profile of Power Types', fontsize=16, fontweight='bold', pad=20)
fig.tight_layout()

# Simplifying legend to only the emission bars
fig.legend(['Emissions'], loc='upper right', bbox_to_anchor=(0.9, 0.9))

plt.show()