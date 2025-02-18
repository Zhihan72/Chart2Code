import matplotlib.pyplot as plt

energy_usage = [30, 25, 15, 20]

colors = ['#AC92EB', '#4FC1E9', '#A0D568', '#FFCE54']
hatches = ['/', '\\', '|', '-']

explode = (0, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    energy_usage, 
    explode=explode, 
    labels=None,  
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
    text.set_text("")  

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_weight('bold')

ax.set_title('')  # Remove title

plt.tight_layout()
plt.show()