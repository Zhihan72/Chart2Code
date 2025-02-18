import matplotlib.pyplot as plt

labels = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geo', 'Ocean', 'Tidal']
sizes = [25, 20, 30, 15, 10, 12, 8]
colors = ['#FF6347', '#4682B4', '#32CD32', '#8A2BE2', '#FFD700', '#FF8C00', '#3CB371']
explode = (0, 0.1, 0, 0, 0, 0, 0)  # Changed exploded slice 

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, 
                                  autopct='%1.1f%%', startangle=90, pctdistance=0.75, 
                                  textprops=dict(color="black"))  # Changed text color and startangle

for text in texts:
    text.set_fontsize(12)  # Changed font size
    text.set_color('navy')  # Changed color
for autotext in autotexts:
    autotext.set_fontsize(10)  # Changed font size
    autotext.set_weight('normal')  # Changed weight

centre_circle = plt.Circle((0,0), 0.50, fc='lightgray')  # Changed circle size and color
fig.gca().add_artist(centre_circle)

plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Added grid
ax.axis('equal')

plt.title("Renewable Energy in EcoLand - '23", fontsize=16, weight='light', y=1.02)  # Changed font size and weight
plt.legend(wedges, labels, title="Energy Sources", loc="upper right", bbox_to_anchor=(1, 1))  # Changed legend location and title
plt.tight_layout()

plt.show()