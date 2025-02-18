import matplotlib.pyplot as plt

regions = ['Rome', 'Phoenicia', 'Carthage', 'Egypt', 'Greece', 'Anatolia']
manuscripts = [180, 110, 80, 200, 120, 90]
colors = ['#ffcc99','#ff9999','#66b3ff','#c2c2f0','#ffb3e6','#99ff99']
explode = (0, 0.1, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(manuscripts, labels=regions, autopct='%1.1f%%', startangle=90, 
                                  colors=colors, explode=explode, wedgeprops=dict(edgecolor='gray', linestyle='--', width=0.4))

for text in texts:
    text.set_size(13)
    text.set_fontweight('normal')
for autotext in autotexts:
    autotext.set_color('darkblue')
    autotext.set_weight('normal')

plt.title('Ancient Manuscripts Distribution around the Mediterranean', 
          fontsize=16, fontweight='normal', pad=30)

ax.grid(True, linestyle='-.', color='lightgrey')

plt.tight_layout()
plt.legend(wedges, regions, loc="upper right", frameon=False)
plt.show()