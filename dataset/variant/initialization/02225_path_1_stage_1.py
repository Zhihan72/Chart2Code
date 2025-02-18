import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal', 'Tidal', 'Other']
energy_share = [33, 25, 20, 12, 5, 3, 2]

# Shuffled colors for the pie chart segments
colors = ['#2ca02c', '#8c564b', '#aec7e8', '#ffcc00', '#1f77b4', '#9467bd', '#ff7f0e']

explode = (0.1, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    energy_share, 
    explode=explode, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops={'edgecolor': 'black'}, 
    shadow=True
)

for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Global Renewable Energy Production in 2023\nDiverse and Sustainable Power Sources', fontsize=16, fontweight='bold', pad=20)

plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()