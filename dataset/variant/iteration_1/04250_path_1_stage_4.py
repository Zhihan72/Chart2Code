import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

model_alpha_sales = np.array([18, 30, 5, 22, 12, 15, 9, 25, 7, 10, 28, 20])
model_beta_sales = np.array([10, 27, 8, 23, 12, 16, 13, 20, 14, 25, 6, 18])
model_gamma_sales = np.array([23, 5, 4, 18, 11, 26, 14, 21, 7, 16, 8, 12])
model_delta_sales = np.array([26, 19, 8, 32, 24, 29, 21, 14, 9, 17, 11, 13])

fig, ax = plt.subplots(figsize=(14, 8))
common_color = '#FF5733'
linestyles = ['-.', '-', ':', '--']
markers = ['d', 'o', 'v', 's']

for sales, linestyle, marker in zip(
    [model_alpha_sales, model_beta_sales, model_gamma_sales, model_delta_sales],
    linestyles, markers):

    ax.plot(months, sales, marker=marker, linestyle=linestyle, linewidth=2, color=common_color)

ax.grid(True, linestyle='-', alpha=0.3)
ax.set_xlim(-0.5, len(months)-0.5)
ax.set_ylim(0, 35)
plt.xticks(np.arange(len(months)), months, rotation=45)
plt.tight_layout()

plt.show()