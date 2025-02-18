import matplotlib.pyplot as plt

regions = ['Asia', 'Europe', 'Africa', 'North America', 'Latin America & Caribbean', 'Oceania']
usage_percentages = [53, 15, 12, 10, 7, 3]

# New colors for each segment
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF9', '#F9FF33']

explode = (0.1, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
plt.pie(usage_percentages, labels=regions, autopct='%1.1f%%', startangle=90, colors=colors, 
        explode=explode, pctdistance=0.85, shadow=True)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Global Internet Users\nDistribution by Region (2023)', fontsize=16, fontweight='bold')
plt.axis('equal')

plt.tight_layout()

plt.show()