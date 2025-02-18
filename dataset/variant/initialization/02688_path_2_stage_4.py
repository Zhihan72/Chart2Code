import matplotlib.pyplot as plt

sectors = [
    'Biotech Future', 
    'A. Electronics', 
    'Green Energy Prod.', 
    'Precision Tools'
]
gdp_contribution = [40, 20, 10, 10]

colors = ['#FF9999', '#66B3FF', '#FFCC99', '#E0E0E0']

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    gdp_contribution,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'linewidth': 0, 'width': 0.3},  # Removed edge color for simplicity
    pctdistance=0.85
)

centre_circle = plt.Circle((0, 0), 0.50, fc='white')
ax.add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.text(0, 0, 'Tech Growth\nSnapshot', fontsize=14, fontweight='bold', ha='center', va='center')

plt.tight_layout()
plt.show()