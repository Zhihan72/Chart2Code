import matplotlib.pyplot as plt
import numpy as np

cuisines = ["Italian", "Japanese", "Mexican", "Indian", "Chinese", "Thai", "French", "Greek", "Spanish", "Middle Eastern"]
popularity_scores = np.array([85, 75, 70, 65, 60, 55, 50, 45, 40, 35])

colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#DAF7A6', '#FFC0CB', '#FF6F61', '#92A8D1', '#B833FF']

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(cuisines, popularity_scores, color=colors, height=0.6)

ax.invert_yaxis()
ax.set_xlim(0, 100)

plt.tight_layout()
plt.show()