import numpy as np
import matplotlib.pyplot as plt

centuries = ['15th Century', '18th Century', '20th Century']
methods = ['Stone Masonry', 'Brickwork', 'Wood Framing', 'Steel Framing']

data = np.array([
    [60, 30, 10, 0],
    [20, 50, 30, 0],
    [10, 20, 30, 40]
])

num_centuries = len(centuries)
bar_width = 0.4

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#FF5733', '#33FF57', '#3357FF', '#F0E68C']

for i in range(num_centuries):
    ax.bar(i + np.arange(len(methods)) * bar_width, data[i], bar_width, color=colors)

plt.tight_layout()
plt.show()