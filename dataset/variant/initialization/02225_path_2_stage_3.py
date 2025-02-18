import matplotlib.pyplot as plt

energy_sources = ['Biomass', 'Geothermal', 'Hydropower', 'Other', 'Solar', 'Tidal', 'Wind']
energy_share = [12, 5, 20, 2, 33, 3, 25]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']
explode = (0, 0.05, 0, 0, 0.1, 0, 0.1)

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    energy_share, 
    explode=explode, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=70, 
    colors=colors, 
    pctdistance=0.8, 
    wedgeprops={'edgecolor': 'gray', 'linestyle': 'dashed'}, 
    shadow=False
)

for text in texts:
    text.set_fontsize(11)
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color('black')
    autotext.set_fontweight('regular')

centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Renewable Energy Production 2023\nSustainable Power Mix Globally', fontsize=18, fontweight='regular', pad=20)
plt.legend(wedges, energy_sources, title="Power Types", loc="best", fancybox=True, shadow=True)
plt.tight_layout()
plt.show()