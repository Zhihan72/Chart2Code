import matplotlib.pyplot as plt

percentages = [25, 20, 15, 10, 5]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#8B008B']
explode = (0, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    percentages, colors=colors, explode=explode,
    autopct='%1.1f%%', startangle=140
)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

plt.axis('equal')
plt.tight_layout()
plt.show()