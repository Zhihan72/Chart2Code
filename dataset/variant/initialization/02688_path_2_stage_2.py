import matplotlib.pyplot as plt

sectors = [
    'Biotech Future', 
    'A. Electronics', 
    'Self-driving Cars', 
    'Green Energy Prod.', 
    'Precision Tools', 
    'Robotic Systems'
]
gdp_contribution = [40, 20, 15, 10, 10, 5]

# New set of colors for each sector
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#E0E0E0', '#B4B4FF']

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    gdp_contribution,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'gray', 'linewidth': 1, 'width': 0.3},
    pctdistance=0.85
)

centre_circle = plt.Circle((0, 0), 0.50, fc='white')
ax.add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.text(0, 0, 'Tech Growth\nSnapshot', fontsize=14, fontweight='bold', ha='center', va='center')

plt.title("Innovative Industry Expansion:\nEconomic Share by Sector", 
          fontsize=16, fontweight='bold', ha='center', pad=20)
plt.legend(wedges, sectors, title="Categories", loc='center left', 
           bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.tight_layout()
plt.show()