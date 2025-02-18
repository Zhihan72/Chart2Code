import matplotlib.pyplot as plt

continents = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
initiatives_percentage = [15, 10, 25, 20, 18, 8, 4]

# New set of colors for each continent
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#5F9EA0', '#D2691E', '#FF7F50', '#9ACD32']

plt.figure(figsize=(12, 8))

explode = (0, 0, 0.1, 0, 0, 0, 0)
plt.pie(initiatives_percentage, labels=continents, autopct='%1.1f%%', startangle=120, colors=colors, shadow=True, explode=explode)

plt.title('Global Exploration Initiatives by Continent\n(A Hypothetical Distribution)', fontsize=18, fontweight='bold', pad=20)
plt.legend(title="Continents", loc='center left', bbox_to_anchor=(1.1, 0.5), fontsize=12)

plt.tight_layout()
plt.show()