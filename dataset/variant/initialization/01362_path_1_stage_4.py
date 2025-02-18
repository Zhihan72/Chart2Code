import matplotlib.pyplot as plt
import numpy as np

cuisines = ["Italian", "Japanese", "Mexican", "Indian", "Chinese", "Thai", "French", "Greek", "Spanish", "Middle Eastern", "Turkish", "Vietnamese"]
popularity_scores = np.array([85, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25])

# Manually shuffled the colors and added new colors for new data
colors = ['#DAF7A6', '#581845', '#FFC300', '#B833FF', '#92A8D1', '#FF6F61', '#C70039', '#900C3F', '#FFC0CB', '#FF5733', '#7F7F7F', '#40E0D0']

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(cuisines, popularity_scores, color=colors, height=0.6)

ax.invert_yaxis()
ax.set_xlim(0, 100)

plt.tight_layout()
plt.show()