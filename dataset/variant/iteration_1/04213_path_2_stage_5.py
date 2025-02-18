import matplotlib.pyplot as plt

household_types = [
    "Shared Apt", "Large Fam", "Single", "Small Fam", "Ret Home"
]
energy_consumption = [
    350, 600, 300, 450, 400
]

fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.bar(household_types, energy_consumption, color=['#4daf4a','#377eb8','#e41a1c','#ff7f00','#984ea3'], edgecolor='black', alpha=0.85)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 10, f'{yval} kWh', ha='center', va='bottom', fontsize=12)

ax.set_title('Energy Use by Household\nEnergio 2023', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Type', fontsize=14)
ax.set_ylabel('Avg Monthly Energy (kWh)', fontsize=14)

plt.tight_layout()

plt.show()