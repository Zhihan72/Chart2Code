import matplotlib.pyplot as plt

regions = ['Asia', 'Europe', 'Africa', 'North America', 'Latin America & Caribbean', 'Oceania']
usage_percentages = [53, 15, 12, 10, 7, 3]

colors = ['#33FFF9', '#FF33A8', '#FF5733', '#3357FF', '#F9FF33', '#33FF57']
explode = (0, 0.1, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
plt.pie(usage_percentages, startangle=140, colors=colors,
        explode=explode, autopct='%1.1f%%')

plt.title('Global Internet Users\nDistribution by Region (2023)', fontsize=14, fontweight='medium')
plt.axis('equal')
plt.show()