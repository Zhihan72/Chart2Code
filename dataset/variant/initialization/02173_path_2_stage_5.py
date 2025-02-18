import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Fossil Fuels', 'Wind', 'Biomass', 'Solar', 'Hydropower']
consumption_2023 = [10, 25, 15, 30, 20]

new_colors = ['#a6d854', '#fc8d62', '#e78ac3', '#66c2a5', '#8da0cb']

fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(
    consumption_2023, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=new_colors,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    pctdistance=0.85
)

plt.setp(autotexts, size=9, weight="bold", color='white')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

ax.set_title('Renewable Energy Consumption Breakdown')

ax.annotate(
    'Rising Wind Contribution',
    xy=(-0.2, 0.4), xytext=(-0.4, 0.6),
    arrowprops=dict(facecolor='red', shrink=0.05),
    fontsize=10, ha='center', color='#329932'
)

plt.tight_layout()
plt.show()