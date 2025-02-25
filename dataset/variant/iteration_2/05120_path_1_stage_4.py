import matplotlib.pyplot as plt
import numpy as np

social_media = [3.2, 2.8, 2.1, 1.5, 0.8]
gaming = [2.4, 1.9, 1.3, 0.8, 0.6]
# Removed the productivity and entertainment data

fig, ax = plt.subplots(figsize=(14, 8))
width = 0.2
y_pos = np.arange(len(social_media))

color = 'slateblue'
ax.barh(y_pos - 1.5 * width, social_media, height=width, color=color)
ax.barh(y_pos - 0.5 * width, gaming, height=width, color=color)

plt.axis('off')
plt.tight_layout()
plt.show()