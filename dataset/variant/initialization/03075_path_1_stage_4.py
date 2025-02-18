import matplotlib.pyplot as plt
import numpy as np

themes = ['Space Exploration', 'Post-Human Evolution', 'Environmental Apocalypse', 'Technological Utopia']
distribution = np.array([25, 10, 20, 30])
colors = ['#FFD700', '#66B3FF', '#FF9999', '#FFCC99']
explode = (0, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(8, 8))
# Creating a donut pie chart by setting a wedgeprops parameter to create a hole
wedges, texts, autotexts = ax.pie(distribution, labels=themes, autopct='%1.1f%%', startangle=120, colors=colors, 
                                  explode=explode, textprops=dict(color="black"), wedgeprops=dict(width=0.3))

plt.setp(autotexts, size=12, weight="normal")
plt.setp(texts, size=8, style='italic')

ax.set_title("Futuristic Literary Themes Distribution", fontsize=16, fontweight='light', loc='right')
ax.legend(wedges, themes, title="Themes", loc="upper right", frameon=False)

plt.tight_layout()
plt.show()