import matplotlib.pyplot as plt

sectors = [
    'Advanced Electronics',
    'Biotechnology',
    'Robotics',
    'Renewable Energy Mfg.',
    'Autonomous Vehicles',
    'Precision Machinery'
]
gdp_contribution = [40, 20, 15, 10, 10, 5]

colors = ['#FFD700', '#8A2BE2', '#FF4500', '#32CD32', '#00CED1', '#FF6347']

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    gdp_contribution,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,  # Altered start angle
    wedgeprops={'edgecolor': 'purple', 'linewidth': 2.5, 'linestyle': '--', 'width': 0.35},
    pctdistance=0.8  # Changed position for percentage labels
)

centre_circle = plt.Circle((0, 0), 0.45, fc='lightgray')  # Changed center circle color and radius
ax.add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('darkblue')  # Altered text color
    autotext.set_fontsize(12)  # Increased font size
    autotext.set_weight('regular')  # Altered font weight

ax.text(0, 0, 'Technotopia\n2023', fontsize=18, fontweight='light', ha='center', va='center') # Changed styling of the central label

plt.title("Industrial Growth in Technotopia:\nGDP Contribution by Manufacturing Sectors", 
          fontsize=20, fontweight='regular', ha='center', pad=20)  # Changed title size and weight

plt.legend(wedges, sectors, title="Sectors", loc='upper right', 
           fontsize=11, frameon=True, shadow=True, fancybox=True, borderpad=1.2)  # Changed legend position and style

plt.grid(True, linestyle=':', linewidth=0.5)  # Added grid

plt.tight_layout()
plt.show()