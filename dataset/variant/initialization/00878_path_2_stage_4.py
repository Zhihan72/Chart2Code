import matplotlib.pyplot as plt

percentages = [25, 20, 15, 10, 5]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#8B008B']
explode = (0.1, 0, 0, 0.1, 0)

plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    percentages, colors=colors, explode=explode,
    autopct='%1.1f%%', startangle=120,
    wedgeprops=dict(edgecolor='black', linewidth=1.5, linestyle='--'),
    textprops=dict(color='navy', fontsize=12)
)

for autotext in autotexts:
    autotext.set_color('darkred')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

plt.legend(wedges, ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4', 'Quarter 5'], title="Quarters", loc="lower left")
plt.grid(axis='y', linestyle=':', linewidth=0.5)

plt.axis('equal')
plt.tight_layout()
plt.show()