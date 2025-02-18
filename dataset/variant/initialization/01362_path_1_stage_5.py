import matplotlib.pyplot as plt
import numpy as np

# Data
cuisines = ["Vietnamese", "Turkish", "Middle Eastern", "Spanish", "Greek",
            "French", "Thai", "Chinese", "Indian", "Mexican", "Japanese", "Italian"]
popularity_scores = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 85])

# Colors aligned with sorted data
colors = ['#40E0D0', '#7F7F7F', '#FF5733', '#FFC0CB', '#900C3F',
          '#C70039', '#FF6F61', '#92A8D1', '#B833FF', '#FFC300',
          '#581845', '#DAF7A6']

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(cuisines, popularity_scores, color=colors, height=0.6)

# The y-axis is already in the order corresponding to the sorted data
ax.set_xlim(0, 100)

plt.tight_layout()
plt.show()