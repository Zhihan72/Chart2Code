import matplotlib.pyplot as plt
import numpy as np

percentages = [30, 25, 15, 10, 5]
colors = ['#f3e5ab', '#7b3f00', '#ff69b4', '#d2b48c', '#93c572']
explode = (0.05, 0.1, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts = ax.pie(
    percentages, 
    startangle=90,
    colors=colors,
    explode=explode,
    wedgeprops=dict(width=0.4, edgecolor='w', lw=2)
)

for text in texts:
    text.set_fontsize(0)  # effectively removes the text

ax.axis('equal')

plt.tight_layout()
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()