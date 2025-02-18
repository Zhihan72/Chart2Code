import matplotlib.pyplot as plt

countries = ['United States', 'European Union', 'China', 'Japan', 'Australia', 'Canada', 'Others', 'India', 'Brazil']
contributions = [25, 20, 18, 15, 10, 7, 5, 12, 8]
missions = [120, 100, 85, 70, 55, 30, 25, 50, 40]
new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Pie chart for contributions
ax1.pie(
    contributions, 
    labels=countries, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=new_colors,
    explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0)
)

# Horizontal bar chart for scientific missions
ax2.barh(countries, missions, color=new_colors)
ax2.set_xlabel('Number of Missions')
ax2.set_xlim(0, max(missions) + 20)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()