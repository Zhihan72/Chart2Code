import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

sectors = ["Residential", "Commercial", "Industrial", "Public Transportation", "Miscellaneous"]
energy_usage = [30, 25, 15, 20, 10]

# Shuffling colors, but maintaining order in the list for deterministic changes
colors = ['#99FF99', '#FF66B3', '#FF9999', '#66B3FF', '#FFCC99']
hatches = ['\\', '+', '/', '-', '|']

explode = (0, 0, 0, 0.1, 0) 

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    energy_usage,
    explode=explode,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    shadow=True,
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3) 
)

for wedge, hatch in zip(wedges, hatches):
    wedge.set_hatch(hatch)

for text in texts:
    text.set_fontsize(10)
    text.set_color('blue')  # Changed text color

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_weight('bold')

# Changed Legend location and border around pie chart
patches = [mpatches.Patch(facecolor=color, hatch=hatch, label=sector)
           for color, hatch, sector in zip(colors, hatches, sectors)]
ax.legend(handles=patches, loc='upper right', fontsize=10, title="Sectors", frameon=True)

# Changed title properties and removed the pad
ax.set_title(
    'Solar Energy Usage: 2050',
    fontsize=14, fontweight='normal', va='bottom', color='darkred'  # Changed title font properties
)

# Added grid to the chart
plt.grid(True)

plt.tight_layout()
plt.show()