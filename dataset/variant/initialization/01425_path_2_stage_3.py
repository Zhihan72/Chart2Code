import matplotlib.pyplot as plt

regions = ['Grc', 'Egy', 'Rom', 'Car', 'Pho', 'Ana']
manuscripts = [120, 200, 180, 80, 110, 90]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode = (0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(manuscripts, labels=regions, autopct='%1.1f%%', startangle=180,
                                  colors=colors, explode=explode, wedgeprops=dict(width=0.4, edgecolor='navy'))

for text in texts:
    text.set_size(13)
    text.set_fontweight('normal')
for autotext in autotexts:
    autotext.set_color('gray')
    autotext.set_weight('light')

plt.title('Ancient Manuscripts\nin the Mediterranean', fontsize=16, fontweight='normal', pad=25)
plt.grid(True, color='lightgrey', linestyle='--')
plt.tight_layout()
plt.legend(wedges, regions, title="Regions", loc="lower right")
plt.show()