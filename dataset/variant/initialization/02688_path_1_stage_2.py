import matplotlib.pyplot as plt

sectors = [
    'Advanced Electronics',
    'Biotechnology',
    'Robotics',
    'Renewable Energy Mfg.',
    'Autonomous Vehicles',
    'Precision Machinery',
    'Artificial Intelligence',
    'Nanotechnology'
]
gdp_contribution = [35, 15, 10, 10, 5, 5, 10, 10]

colors = ['#FFD700', '#8A2BE2', '#FF4500', '#32CD32', '#00CED1', '#FF6347', '#DA70D6', '#4169E1']

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    gdp_contribution,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops={'edgecolor': 'purple', 'linewidth': 2.5, 'linestyle': '--', 'width': 0.35},
    pctdistance=0.8
)

centre_circle = plt.Circle((0, 0), 0.45, fc='lightgray')
ax.add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('darkblue')
    autotext.set_fontsize(12)
    autotext.set_weight('regular')

ax.text(0, 0, 'Technotopia\n2023', fontsize=18, fontweight='light', ha='center', va='center')

plt.title("Industrial Growth in Technotopia:\nGDP Contribution by Manufacturing Sectors",
          fontsize=20, fontweight='regular', ha='center', pad=20)

plt.legend(wedges, sectors, title="Sectors", loc='upper right',
           fontsize=11, frameon=True, shadow=True, fancybox=True, borderpad=1.2)

plt.grid(True, linestyle=':', linewidth=0.5)

plt.tight_layout()
plt.show()