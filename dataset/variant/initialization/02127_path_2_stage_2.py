import matplotlib.pyplot as plt

energy_sources = ['Hydropower', 'Biomass', 'Solar', 'Wind', 'Geothermal']
energy_shares = [20, 10, 35, 30, 5]
colors = ['#4682B4', '#8B4513', '#FFD700', '#87CEEB', '#556B2F']
explode = (0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(9, 9))

# Change pie chart to a donut chart by adding a circle at the center
wedges, texts, autotexts = ax.pie(
    energy_shares, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=100, 
    colors=colors, 
    explode=explode, 
    shadow=True
)

# Add a white circle at the center to create a hole, forming a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')

ax.set_title(
    'Energy Division of Renewables\nfor 2023', 
    fontsize=16, 
    fontweight='bold', 
    pad=30
)

ax.axis('equal')

plt.legend(
    wedges, energy_sources,
    title="Source Categories",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=12
)

plt.tight_layout()
plt.show()