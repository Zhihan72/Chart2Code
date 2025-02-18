import matplotlib.pyplot as plt
import numpy as np

social_media = [3.2, 2.8, 2.1, 1.5, 0.8]
gaming = [2.4, 1.9, 1.3, 0.8, 0.6]
productivity = [1.2, 1.5, 1.8, 2.3, 1.9]
entertainment = [2.1, 2.4, 2.0, 1.5, 1.2]

fig, ax = plt.subplots(figsize=(14, 8))
width = 0.2
y_pos = np.arange(len(social_media))

ax.barh(y_pos - 1.5*width, social_media, height=width, color='royalblue')
ax.barh(y_pos - 0.5*width, gaming, height=width, color='tomato')
ax.barh(y_pos + 0.5*width, productivity, height=width, color='forestgreen')
ax.barh(y_pos + 1.5*width, entertainment, height=width, color='gold')

def add_values(bars):
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.1, bar.get_y() + bar.get_height() / 2, f'{width:.1f}', va='center', fontsize=10)

plt.axis('off')
plt.tight_layout()
plt.show()