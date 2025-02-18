import matplotlib.pyplot as plt
import numpy as np

sectors = ['Tidal Power', 'Geothermal Energy', 'Hydrogen Fuel Cells', 'Bioenergy']
power_sources = ['Tidal Generators', 'Hydrothermal Vents', 'Hydrogen Cells', 'Biomass']

energy_data = [
    [50, 10, 20, 20],  
    [10, 60, 20, 10],  
    [20, 20, 40, 20],  
    [20, 10, 20, 50]   
]

efficiency_ratios = [0.8, 0.6, 0.9, 0.7]

colors = ['#81C784', '#FF8A65', '#64B5F6', '#FFD54F']

fig, ax = plt.subplots(2, 2, figsize=(16,16))
plt.subplots_adjust(top=0.85)
fig.suptitle("Underwater City Energy Distribution and Efficiency\nYear 2145", fontsize=18, fontweight='bold', y=0.98)

explode = (0.1, 0, 0, 0)

for i, sector in enumerate(sectors):
    wedges, texts, autotexts = ax.flatten()[i].pie(
        energy_data[i],
        labels=power_sources,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        explode=explode,
        textprops=dict(color="black")
    )
    for text in texts:
        text.set_fontsize(10)
    for autotext in autotexts:
        autotext.set_fontsize(10)
    ax.flatten()[i].set_title(f"{sector} Energy Sources", fontsize=14, fontweight='bold')

ax_eff = fig.add_subplot(224)
bars = ax_eff.bar(sectors, efficiency_ratios, color=colors)

ax_eff.set_ylabel('Efficiency Ratio (arbitrary units)', fontsize=12, fontweight='bold')
ax_eff.set_xlabel('Energy Sectors', fontsize=12, fontweight='bold')
ax_eff.set_title('Efficiency Comparison of\nEnergy Sectors in the Underwater City', fontsize=16, fontweight='bold', pad=20)

for bar, efficiency in zip(bars, efficiency_ratios):
    ax_eff.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02, f'{efficiency:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax_eff.set_xticklabels(sectors, rotation=45, ha='right', fontsize=10, fontweight='bold')

plt.tight_layout(rect=[0, 0, 0.85, 0.95])
plt.show()