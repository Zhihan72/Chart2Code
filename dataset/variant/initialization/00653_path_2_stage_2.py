import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

energy_usage = [30, 25, 15, 20, 10]

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF66B3']
hatches = ['/', '\\', '|', '-', '+']

explode = (0, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    energy_usage, 
    explode=explode, 
    labels=None,  # Removed labels
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
    text.set_text("")  # Remove texts

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_weight('bold')

ax.legend().remove()  # Removed the legend

ax.set_title('')  # Remove title

plt.tight_layout()
plt.show()