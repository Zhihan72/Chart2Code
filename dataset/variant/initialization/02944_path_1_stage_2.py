import matplotlib.pyplot as plt

energy_sources = ['Solar Energy', 'Wind Energy', 'Hydroelectric', 'Biomass', 'Fossil Fuels', 'Nuclear', 'Geothermal', 'Hydrogen']
energy_distribution = [20, 15, 10, 8, 18, 9, 12, 8]
colors = ['#FFDB58', '#32CD32', '#4682B4', '#8B4513', '#808080', '#B0C4DE', '#D2691E', '#FF6347']

fig, ax = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax.pie(
    energy_distribution, labels=energy_sources, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85,
    explode=(0.05, 0.04, 0.06, 0.07, 0.04, 0.05, 0.03, 0.06),  
    wedgeprops=dict(width=0.25, linestyle='--'), shadow=True
)

for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('normal')

for autotext in autotexts:
    autotext.set_color('darkblue')
    autotext.set_fontsize(9)
    autotext.set_fontweight('normal')

ax.axis('equal')
ax.set_title('Energy Mix in a Sustainable City\n2023', fontsize=14, fontweight='normal', pad=25)

ax.legend(wedges, energy_sources, loc='upper right', bbox_to_anchor=(1.1, 1.0), title="Sources", fontsize='x-small', title_fontsize='10')
ax.grid(True, which='major', color='grey', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.show()