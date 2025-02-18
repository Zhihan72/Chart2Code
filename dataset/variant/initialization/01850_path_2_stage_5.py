import numpy as np
import matplotlib.pyplot as plt

centuries = ['15th Century', '18th Century', '20th Century']
methods = ['Stone Masonry', 'Brickwork', 'Wood Framing', 'Steel Framing']

# Manually altering the data within each group randomly while preserving the dimensions
data = np.array([
    [30, 10, 60, 0],  # Altered values within the first century
    [50, 30, 0, 20],  # Altered values within the second century
    [20, 40, 10, 30]  # Altered values within the third century
])

num_centuries = len(centuries)
bar_width = 0.4

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#FF5733', '#33FF57', '#3357FF', '#F0E68C']

for i in range(num_centuries):
    ax.bar(i + np.arange(len(methods)) * bar_width, data[i], bar_width, color=colors)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.axis('off')

plt.tight_layout()
plt.show()