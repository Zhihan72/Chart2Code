import matplotlib.pyplot as plt
import numpy as np

themes = ['Space Exploration', 'Post-Human Evolution', 'Environmental Apocalypse', 'Technological Utopia']
distribution = np.array([25, 10, 20, 30])
colors = ['#FFD700', '#66B3FF', '#FF9999', '#FFCC99']  # Shuffled colors
explode = (0, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(distribution, labels=themes, autopct='%1.1f%%', startangle=120, colors=colors,
                                  explode=explode, textprops=dict(color="black"))

plt.setp(autotexts, size=12, weight="normal")
plt.setp(texts, size=8, style='italic')

ax.set_title("Futuristic Literary Themes Distribution", fontsize=16, fontweight='light', loc='right')

# Altering legend position and removing the border
ax.legend(wedges, themes, title="Themes", loc="upper right", frameon=False)

# Adding grid to the plot (Note: grids do not typically apply to pie charts in matplotlib)
ax.grid(True, linestyle='-', linewidth=0.5, color='gray', alpha=0.7)

plt.tight_layout()
plt.show()