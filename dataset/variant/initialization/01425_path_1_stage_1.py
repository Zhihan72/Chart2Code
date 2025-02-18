import matplotlib.pyplot as plt

regions = ['Rome', 'Phoenicia', 'Carthage', 'Egypt', 'Greece', 'Anatolia']
manuscripts = [180, 110, 80, 200, 120, 90]
colors = ['#ffcc99','#ffb3e6','#66b3ff','#c2c2f0','#ff9999','#99ff99']
explode = (0, 0, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(manuscripts, labels=regions, autopct='%1.1f%%', startangle=140, 
                                  colors=colors, explode=explode, wedgeprops=dict(edgecolor='black'))

for text in texts:
    text.set_size(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

plt.title('Around the Mediterranean: Manuscripts\nAncient Found Distribution', 
          fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.legend(wedges, regions, title="Regions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()