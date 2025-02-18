import matplotlib.pyplot as plt
import numpy as np

countries = ['US', 'EU', 'CN', 'JP', 'AU', 'CA', 'Other']
contributions = [25, 20, 18, 15, 10, 7, 5]
missions = [120, 100, 85, 70, 55, 30, 25]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle("2023 Ocean Missions\nContributions & Execute Count", fontsize=18, fontweight='bold', color='#333')

ax1.barh(countries, missions, color=colors)
ax1.set_xlabel('Missions', fontsize=12, fontweight='bold')
ax1.set_title("Missions by Country", fontsize=14, fontweight='bold', color='#555')
ax1.grid(axis='x', linestyle='--', alpha=0.7)
ax1.set_xlim(0, max(missions) + 20)

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

ax2.set_title("Contributions", fontsize=14, fontweight='bold', color='#555')

ax2.annotate(
    'Leader',
    xy=(0.9, 0.3),
    xytext=(1.5, 0.5),
    arrowprops=dict(facecolor='black', arrowstyle='->'),
    fontsize=10,
    fontweight='bold',
    color='black'
)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()