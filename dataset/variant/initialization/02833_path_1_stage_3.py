import matplotlib.pyplot as plt

countries = ['United States', 'European Union', 'China', 'Japan', 'Australia', 'Canada', 'Others', 'India', 'Brazil']
contributions = [25, 20, 18, 15, 10, 7, 5, 12, 8]
missions = [120, 100, 85, 70, 55, 30, 25, 50, 40]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#17becf', '#bcbd22']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Pie chart for contributions
ax1.pie(
    contributions, 
    labels=countries, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0)
)

# Horizontal bar chart for scientific missions
ax2.barh(countries, missions, color=colors)
ax2.set_xlabel('Number of Missions')
ax2.set_xlim(0, max(missions) + 20)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()