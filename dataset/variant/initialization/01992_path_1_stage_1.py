import matplotlib.pyplot as plt

# Define the data for the pie chart
continents = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
initiatives_percentage = [15, 10, 25, 20, 18, 8, 4]

# Define a new set of colors for each continent
new_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF3', '#A833FF', '#FFF333']

plt.figure(figsize=(12, 8))

explode = (0, 0, 0.1, 0, 0, 0, 0)
plt.pie(initiatives_percentage, labels=continents, autopct='%1.1f%%', startangle=120, colors=new_colors, shadow=True, explode=explode)

plt.title('Global Exploration Initiatives by Continent\n(A Hypothetical Distribution)', fontsize=18, fontweight='bold', pad=20)

plt.legend(title="Continents", loc='center left', bbox_to_anchor=(1.1, 0.5), fontsize=12)

plt.tight_layout()

plt.show()