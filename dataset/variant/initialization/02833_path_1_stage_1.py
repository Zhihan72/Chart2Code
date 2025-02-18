import matplotlib.pyplot as plt
import numpy as np

countries = ['United States', 'European Union', 'China', 'Japan', 'Australia', 'Canada', 'Others']
contributions = [25, 20, 18, 15, 10, 7, 5]
missions = [120, 100, 85, 70, 55, 30, 25]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
fig.suptitle("2023 Global Contributions to Ocean Exploration Missions\nwith Number of Missions Executed", fontsize=18, fontweight='bold', color='#333')

wedges, texts, autotexts = ax1.pie(
    contributions, 
    labels=countries, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=(0.1, 0, 0, 0, 0, 0, 0),
    shadow=True,
    textprops=dict(color="white", fontsize=9, weight="bold")
)

ax1.set_title("Contribution by Country/Region", fontsize=14, fontweight='bold', color='#555')

ax1.annotate(
    'Leading Contributor',
    xy=(0.9, 0.3),
    xytext=(1.5, 0.5),
    arrowprops=dict(facecolor='black', arrowstyle='->'),
    fontsize=10,
    fontweight='bold',
    color='black'
)

ax2.barh(countries, missions, color=colors)
ax2.set_xlabel('Number of Missions', fontsize=12, fontweight='bold')
ax2.set_title("Scientific Missions Conducted", fontsize=14, fontweight='bold', color='#555')
ax2.grid(axis='x', linestyle='--', alpha=0.7)
ax2.set_xlim(0, max(missions) + 20)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()