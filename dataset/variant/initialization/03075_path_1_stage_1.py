import matplotlib.pyplot as plt
import numpy as np

themes = ['Technological Utopia', 'Environmental Apocalypse', 'Space Exploration', 'Post-Human Evolution']
distribution = np.array([30, 20, 25, 10])
colors = ['#FF9999', '#66B3FF', '#FFCC99', '#FFD700']
explode = (0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(distribution, labels=themes, autopct='%1.1f%%', startangle=140, colors=colors,
                                  explode=explode, textprops=dict(color="black"))

plt.setp(autotexts, size=10, weight="bold")
plt.setp(texts, size=9)

ax.set_title("Distribution of Themes in Futuristic Literature\n(Last Decade)", fontsize=14, fontweight='bold', pad=20)
ax.legend(wedges, themes, title="Themes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()