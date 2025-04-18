import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Geothermal', 'Tidal Energy', 'Nuclear Energy']
sizes = [20, 15, 25, 10, 5, 5, 20]  # Adjusted size for existing and new data
colors = ['#FFD700', '#1E90FF', '#228B22', '#8B4513', '#FF4500', '#4B0082', '#F08080']
explode = (0.1, 0, 0.1, 0, 0, 0, 0)  # Explode the two largest sections

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85, textprops=dict(color="w"))

for text in texts:
    text.set_fontsize(10)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_weight('bold')

centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')  

plt.title("Distribution of Renewable and Nuclear Energy Sources\nin EcoLand - 2023", fontsize=14, weight='bold', y=1.05)

plt.legend(wedges, labels, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()

plt.show()