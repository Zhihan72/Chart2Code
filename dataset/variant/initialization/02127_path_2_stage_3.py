import matplotlib.pyplot as plt

energy_sources = ['Hydropower', 'Biomass', 'Solar', 'Wind', 'Geothermal']
energy_shares = [20, 10, 35, 30, 5]
colors = ['#4682B4', '#8B4513', '#FFD700', '#87CEEB', '#556B2F']
explode = (0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(9, 9))

wedges, texts, autotexts = ax.pie(
    energy_shares,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=100,
    colors=colors,
    explode=explode,
    shadow=False
)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')

ax.axis('equal')

plt.show()