import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

centuries = ['15th Century', '18th Century', '20th Century']
methods = ['Stone Masonry', 'Brickwork', 'Wood Framing', 'Steel Framing']

data = np.array([
    [60, 30, 10, 0],
    [20, 50, 30, 0],
    [10, 20, 30, 40]
])

num_centuries = len(centuries)
num_methods = len(methods)

x_pos = np.arange(num_centuries)
y_pos = np.arange(num_methods)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Manually shuffled colors assignment
colors = ['#E7298A', '#7B9F35', '#D95F02', '#7570B3']

for i, (color, method) in enumerate(zip(colors, methods)):
    ax.bar3d(x_pos, i * np.ones(num_centuries), np.zeros(num_centuries), 0.4, 0.4, data[:, i],
             color=color, alpha=0.8, label=method)

ax.set_xlabel('Centuries', labelpad=15)
ax.set_ylabel('Construction Methods', labelpad=15)
ax.set_zlabel('Prevalence (%)', labelpad=10)
ax.set_title('Evolution of Construction Methods\nAcross Centuries', fontsize=16, pad=30)

ax.set_xticks(x_pos + 0.2)
ax.set_xticklabels(centuries, fontsize=10, rotation=25, ha='right')
ax.set_yticks(y_pos)
ax.set_yticklabels(methods, fontsize=10)

ax.legend(title='Methods', loc='upper left', bbox_to_anchor=(0.9, 1.0), fontsize=9)

ax.view_init(elev=25, azim=-50)

plt.tight_layout()
plt.show()