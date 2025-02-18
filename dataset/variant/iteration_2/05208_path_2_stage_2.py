import matplotlib.pyplot as plt
import numpy as np

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Cookie Dough', 'Pistachio']
percentages = [30, 25, 15, 10, 5]
colors = ['#f3e5ab', '#7b3f00', '#ff69b4', '#d2b48c', '#93c572']
explode = (0.05, 0.1, 0, 0, 0.1)  # Different explode pattern

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=flavors, 
    autopct='%1.1f%%', 
    startangle=90,  # Changed start angle for a new look
    colors=colors, 
    explode=explode, 
    shadow=False,  # Removed shadow for a cleaner look
    wedgeprops=dict(width=0.4, edgecolor='w', lw=2)  # Add width and edge color
)

for text in texts:
    text.set_fontsize(11)
    text.set_fontstyle('italic')  # Change style to italic

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('blue')  # Changed text color for contrast

ax.set_title(
    'Favorite Ice Cream Flavors Among Kids in Summer Camp', 
    fontsize=15, 
    fontweight='medium', 
    pad=20
)

ax.axis('equal')

plt.legend(
    wedges, flavors,
    title="Ice Cream Flavors",
    loc="upper right",  # Moved legend to the top-right corner
    fontsize=10,
    ncol=1,
    frameon=True,  # Added frame to legend
    fancybox=True,
    shadow=True  # Added shadow to the legend
)

plt.tight_layout()
plt.grid(axis='y', linestyle='--', linewidth=0.5)  # Adding grid lines
plt.show()