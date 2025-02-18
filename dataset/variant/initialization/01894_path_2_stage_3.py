import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Wind', 'Fusion', 'Solar', 'Geothermal', 'Hydrogen', 'Fossil Fuels']
energy_usage = np.array([15, 20, 25, 10, 20, 10])

# Use a single color for all sections
single_color = '#4682B4'  # Steel Blue
patterns = ["||", "\\\\", "//", "-", "+", "x"]

explode = (0, 0, 0.1, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    energy_usage,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=90,
    colors=[single_color] * len(energy_sources),
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w', hatch=patterns[2])
)

plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=10, weight='bold')

plt.title(
    'Intergalactic Power Landscape:\nExploration of Energy Utilization in the 22nd Century',
    fontsize=16, weight='bold', pad=20
)

ax_inset = fig.add_axes([0.75, 0.7, 0.15, 0.15], aspect='equal')
inset_data = np.array([30, 20, 15, 25, 10])
inset_labels = ['2025', '2030', '2020', '2040', '2035']
ax_inset.pie(
    inset_data, labels=inset_labels, startangle=90, colors=[single_color] * len(inset_labels),
    autopct='%1.0f%%', wedgeprops=dict(width=0.3, edgecolor='w')
)
ax_inset.set_title('Projection Trajectory', fontsize=8, weight='bold')

plt.tight_layout()
plt.show()