import matplotlib.pyplot as plt

energy_sources = ['Solar Energy', 'Wind Energy', 'Hydroelectric', 'Biomass', 'Fossil Fuels', 'Nuclear']
energy_distribution = [25, 20, 15, 10, 20, 10]
single_color = '#4682B4'  # Consistent single color for all data groups

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    energy_distribution, labels=energy_sources, colors=[single_color]*len(energy_sources),
    autopct='%1.1f%%', startangle=140, explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
)

ax.set_title('Energy Mix in a Sustainable City\n2023', fontsize=16, fontweight='bold', pad=20)

plt.show()