import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Fossil', 'Nuclear', 'Geo', 'Hydrogn']
energy_distribution = [20, 15, 10, 8, 18, 9, 12, 8]

colors = ['#4682B4', '#FF6347', '#FFDB58', '#D2691E', '#32CD32', '#808080', '#8B4513', '#B0C4DE']

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    energy_distribution, labels=energy_sources, colors=colors,
    autopct='%1.1f%%', startangle=140, shadow=True
)

ax.axis('equal')
ax.set_title('City Energy Mix\n2023', fontsize=14, fontweight='normal', pad=25)

ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.0), title="Sources", fontsize='x-small', title_fontsize='10')

plt.tight_layout()
plt.show()