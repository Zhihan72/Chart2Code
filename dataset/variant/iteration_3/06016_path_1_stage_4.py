import matplotlib.pyplot as plt
import numpy as np

devices = ['Wearables', 'Smart TVs', 'Smartphones', 'Gaming Consoles', 'E-Readers', 'Tablets', 'Laptops']
usage_percentage = [8, 10, 35, 7, 5, 15, 25]
colors = ['#ffcc99', '#99ff99', '#66b3ff', '#ff9999', '#9966ff', '#c0c0c0', '#ff6666']
explode = (0, 0, 0.1, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    usage_percentage,
    labels=devices,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    wedgeprops=dict(edgecolor='gray', linewidth=1.5, linestyle='--'),
    pctdistance=0.8
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='blue', linestyle='-.')

fig.gca().add_artist(centre_circle)

ax.axis('equal')

ax.set_title("GadgetWorld Usage Overview\nElectronic Gadgets Utilized", fontsize=14, fontweight='normal', pad=10)

plt.setp(autotexts, size=9, weight='normal', color='navy')
plt.setp(texts, size=11, color='darkred', weight='bold')

ax.legend(
    wedges, devices,
    title="Gadget Types", 
    loc="upper right", bbox_to_anchor=(1.1, 1), fontsize=9,
    frameon=False
)

plt.grid(True, which='both', linestyle=':', linewidth=0.5, color='gray')

plt.tight_layout()

plt.show()