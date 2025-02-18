import matplotlib.pyplot as plt

labels = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geo', 'Ocean', 'Tidal']
sizes = [25, 20, 30, 15, 10, 12, 8]
# New color palette applied to replace original ones
colors = ['#FF6347', '#4682B4', '#32CD32', '#8A2BE2', '#FFD700', '#FF8C00', '#3CB371']
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, 
                                  autopct='%1.1f%%', startangle=140, pctdistance=0.85, 
                                  textprops=dict(color="w"))

for text in texts:
    text.set_fontsize(10)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_weight('bold')

centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.title("Renewable Energy in EcoLand - '23", fontsize=14, weight='bold', y=1.05)
plt.legend(wedges, labels, title="Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()

plt.show()