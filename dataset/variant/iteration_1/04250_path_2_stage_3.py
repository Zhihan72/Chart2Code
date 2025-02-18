import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

model_alpha_sales = np.array([5, 7, 9, 10, 12, 15, 18, 20, 22, 25, 28, 30])
model_beta_sales = np.array([6, 8, 10, 12, 13, 14, 16, 18, 20, 23, 25, 27])
model_gamma_sales = np.array([4, 5, 7, 8, 11, 12, 14, 16, 18, 21, 23, 26])
model_delta_sales = np.array([8, 9, 11, 13, 14, 17, 19, 21, 24, 26, 29, 32])

fig, ax = plt.subplots(figsize=(14, 8))

# Updated set of colors
new_colors = ['#FF6699', '#66FF66', '#6699FF', '#FF9933']
linestyles = ['-', '--', '-.', ':']
markers = ['o', 'v', 's', 'd']

for sales, color, linestyle, marker in zip(
    [model_alpha_sales, model_beta_sales, model_gamma_sales, model_delta_sales],
    new_colors, linestyles, markers):
    
    ax.plot(months, sales, marker=marker, linestyle=linestyle, linewidth=2, color=color)

ax.set_xlim(-0.5, len(months)-0.5)
ax.set_ylim(0, 35)

plt.xticks(np.arange(len(months)), months, rotation=45)
plt.tight_layout()

plt.show()