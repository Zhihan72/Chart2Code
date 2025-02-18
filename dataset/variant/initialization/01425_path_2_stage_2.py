import matplotlib.pyplot as plt

regions = ['Grc', 'Egy', 'Rom', 'Car', 'Pho', 'Ana']
manuscripts = [120, 200, 180, 80, 110, 90]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode = (0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(manuscripts, labels=regions, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, wedgeprops=dict(width=0.3, edgecolor='black'))

for text in texts:
    text.set_size(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

plt.title('Ancient Manuscripts\nin the Mediterranean', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.legend(wedges, regions, title="Regions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()