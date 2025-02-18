import matplotlib.pyplot as plt

regions = ['Asia', 'Europe', 'Africa', 'North America', 'Latin America & Caribbean', 'Oceania', 'Antarctica', 'Atlantis']
usage_percentages = [53, 15, 12, 10, 7, 3, 0.1, 0.9]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6347', '#A9A9A9', '#8A2BE2']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
plt.pie(usage_percentages, labels=regions, autopct='%1.1f%%', startangle=90, colors=colors, 
        explode=explode, shadow=True)

plt.title('Global Internet Users\nDistribution by Region (2023)', fontsize=16, fontweight='bold')
plt.axis('equal')

plt.tight_layout()
plt.show()