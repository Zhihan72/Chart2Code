import matplotlib.pyplot as plt

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']

transportation_emissions = [28, 26, 30, 25, 27]
industry_emissions = [35, 32, 37, 40, 33]
agriculture_emissions = [23, 25, 22, 20, 27]
residential_emissions = [12, 15, 14, 15, 14]

fig, ax = plt.subplots(figsize=(7, 7))
fig.suptitle('Greenhouse Gas Emissions Trends by Sector (1980s-2020s)', fontsize=16, fontweight='bold')

ax.plot(decades, transportation_emissions, marker='o', linestyle='-', linewidth=2, color='green')
ax.plot(decades, industry_emissions, marker='s', linestyle='-', linewidth=2, color='orange')
ax.plot(decades, agriculture_emissions, marker='^', linestyle='-', linewidth=2, color='red')
ax.plot(decades, residential_emissions, marker='d', linestyle='-', linewidth=2, color='blue')

ax.set_title('Emissions by Sector', fontsize=14, fontweight='bold')
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Percentage of Total Emissions', fontsize=12)

# Remove grid lines and legend
# ax.legend(loc='upper right', fontsize=10, frameon=False)
# ax.grid(True, linestyle='--', alpha=0.7)

for i, txt in enumerate(transportation_emissions):
    ax.annotate(f'{txt}%', (decades[i], transportation_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(industry_emissions):
    ax.annotate(f'{txt}%', (decades[i], industry_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(agriculture_emissions):
    ax.annotate(f'{txt}%', (decades[i], agriculture_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(residential_emissions):
    ax.annotate(f'{txt}%', (decades[i], residential_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()