import matplotlib.pyplot as plt

labels = ['Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Geothermal', 'Tidal Energy', 'Nuclear Energy']
sizes = [20, 15, 25, 10, 5, 5, 20]
colors = ['#FFD700', '#1E90FF', '#228B22', '#8B4513', '#FF4500', '#4B0082', '#F08080']
explode = (0.1, 0, 0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
    startangle=120, pctdistance=0.85, textprops=dict(color="w"), 
    wedgeprops=dict(edgecolor='grey', linestyle='--', linewidth=1.2)
)

for text in texts:
    text.set_fontsize(10)
    text.set_color('navy')  # Changed from black to navy
for autotext in autotexts:
    autotext.set_fontsize(9)  # Modified fontsize
    autotext.set_weight('light')  # Changed weight

centre_circle = plt.Circle((0, 0), 0.70, fc='whitesmoke')
fig.gca().add_artist(centre_circle)

ax.axis('equal')  

plt.title("Energy Sources Distribution - EcoLand 2023", fontsize=15, weight='bold', y=1.03)

plt.legend(wedges, labels, title="Energy Types", loc="upper right", fontsize=8)  # Changed legend position and fontsize

ax.grid(True, linestyle=':', linewidth=0.5)  # Added grid with a specific style

plt.tight_layout()

plt.show()