import matplotlib.pyplot as plt

# Data for renewable energy production in 2023
energy_sources = ['Biomass', 'Geothermal', 'Hydropower', 'Other', 'Solar', 'Tidal', 'Wind']
energy_share = [12, 5, 20, 2, 33, 3, 25]

colors = ['#2ca02c', '#ff7f0e', '#aec7e8', '#8c564b', '#ffcc00', '#9467bd', '#1f77b4']
explode = (0, 0, 0, 0, 0.1, 0, 0)

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

plt.title('Renewable Energy Production 2023\nSustainable Power Mix Globally', fontsize=16, fontweight='bold', pad=20)

plt.legend(wedges, energy_sources, title="Power Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()