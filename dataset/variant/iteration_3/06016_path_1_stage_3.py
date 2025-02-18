import matplotlib.pyplot as plt
import numpy as np

devices = ['Wearables', 'Smart TVs', 'Smartphones', 'Gaming Consoles', 'E-Readers', 'Tablets', 'Laptops']
usage_percentage = [8, 10, 35, 7, 5, 15, 25]
colors = ['#ffcc99', '#99ff99', '#66b3ff', '#ff9999', '#9966ff', '#c0c0c0', '#ff6666']
explode = (0, 0, 0.1, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    usage_percentage,
    labels=devices,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    wedgeprops=dict(edgecolor='white', linewidth=2),
    pctdistance=0.85
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

ax.set_title("GadgetWorld Usage Overview:\nVariety of Electronic Gadgets Utilized", fontsize=16, fontweight='bold', pad=20)

plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=12)

ax.text(
    0, 0, 
    '2023 Gadget\nUtilization\nInsights', 
    ha='center', va='center', 
    fontsize=12, color='black', weight='bold'
)

ax.legend(
    wedges, devices,
    title="Gadget Types", 
    loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10
)

plt.tight_layout()

plt.show()