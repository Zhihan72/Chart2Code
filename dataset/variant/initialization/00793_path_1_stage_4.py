import matplotlib.pyplot as plt

art_movements = ['Renaiss.', 'Baroque', 'Romant.', 'Impress.', 'Contemp.']
color_usage = [22, 18, 25, 15, 20]

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%',
                                  startangle=140, shadow=True, explode=(0.05,) * 5)

plt.setp(autotexts, size=9, weight='bold', color='white')

plt.title("Palette of Emotions", fontsize=14, fontweight='bold')

ax.axis('equal')

ax.legend(wedges, art_movements,
          title="Art Styles", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

plt.tight_layout()
plt.show()