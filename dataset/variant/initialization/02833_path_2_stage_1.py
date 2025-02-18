import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
countries = ['United States', 'European Union', 'China', 'Japan', 'Australia', 'Canada', 'Others']
contributions = [25, 20, 18, 15, 10, 7, 5]

# Additional data for the bar chart
missions = [120, 100, 85, 70, 55, 30, 25]  # Hypothetical number of missions per country

# Colors for each section of the pie chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Creating the figure and the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle("2023 Global Contributions to Ocean Exploration Missions\nwith Number of Missions Executed", fontsize=18, fontweight='bold', color='#333')

# Bar chart is now placed on the left
ax1.barh(countries, missions, color=colors)
ax1.set_xlabel('Number of Missions', fontsize=12, fontweight='bold')
ax1.set_title("Scientific Missions Conducted", fontsize=14, fontweight='bold', color='#555')
ax1.grid(axis='x', linestyle='--', alpha=0.7)
ax1.set_xlim(0, max(missions) + 20)

# Pie chart is now placed on the right
wedges, texts, autotexts = ax2.pie(
    contributions, 
    labels=countries, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=(0.1, 0, 0, 0, 0, 0, 0),
    shadow=True,
    textprops=dict(color="white", fontsize=9, weight="bold")
)

ax2.set_title("Contribution by Country/Region", fontsize=14, fontweight='bold', color='#555')

# Annotating the largest contributor in the pie chart
ax2.annotate(
    'Leading Contributor',
    xy=(0.9, 0.3),
    xytext=(1.5, 0.5),
    arrowprops=dict(facecolor='black', arrowstyle='->'),
    fontsize=10,
    fontweight='bold',
    color='black'
)

# Ensuring all text fits and is readable
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the final chart
plt.show()