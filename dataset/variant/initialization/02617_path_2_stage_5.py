import matplotlib.pyplot as plt
import numpy as np

# Mock data
categories = ['A', 'B', 'C']
values = [10, 20, 15]

# Original color assignments for illustration
original_colors = ['blue', 'green', 'red']

# Shuffled colors (manually assigned without using random)
shuffled_colors = ['red', 'blue', 'green']

fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(categories, values, color=shuffled_colors)
ax.set_ylabel('Output (units)', fontsize=12)

plt.tight_layout()
plt.show()