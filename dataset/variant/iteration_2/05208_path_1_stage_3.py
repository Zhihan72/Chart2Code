import matplotlib.pyplot as plt

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Pistachio']
percentages = [30, 25, 15, 5]
colors = ['#f3e5ab', '#7b3f00', '#ff69b4', '#93c572']
explode = (0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=flavors,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops=dict(width=0.3)
)

for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('black')

ax.axis('equal')
plt.show()