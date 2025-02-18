import matplotlib.pyplot as plt

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
initiatives_percentage = [15, 25, 20, 18, 8, 4]

colors = ['#4682B4', '#D2691E', '#FF7F50', '#32CD32', '#FFD700', '#8A2BE2']

plt.figure(figsize=(10, 8))

explode = (0, 0.1, 0.2, 0, 0, 0)
wedges, texts, autotexts = plt.pie(initiatives_percentage, labels=continents, autopct='%1.1f%%',
                                   startangle=140, colors=colors, shadow=False, explode=explode,
                                   wedgeprops=dict(edgecolor='black'))

# Draw a circle at the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Global Exploration Initiatives by Continent',
          fontsize=16, fontfamily='serif', pad=15)

plt.legend(title="Continents", loc='upper right', fontsize=10)

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()