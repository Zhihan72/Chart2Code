import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

spring_density = np.array([
    [10, 15, 11, 14, 12], 
    [20, 23, 18, 21, 22], 
    [30, 35, 32, 28, 33],
    [25, 26, 28, 27, 24],
    [15, 16, 14, 13, 17]
])

summer_density = np.array([
    [12, 18, 13, 16, 14], 
    [22, 25, 20, 23, 24], 
    [32, 37, 34, 30, 35],
    [27, 28, 30, 29, 26],
    [17, 18, 16, 15, 19]
])

winter_density = np.array([
    [8, 12, 9, 11, 10], 
    [18, 21, 16, 19, 20], 
    [28, 33, 30, 26, 31],
    [23, 24, 26, 25, 22],
    [13, 14, 12, 11, 15]
])

fig, axs = plt.subplots(3, 1, figsize=(10, 15), tight_layout=True)

def create_density_plot(ax, data):
    sns.violinplot(data=data, ax=ax, linewidth=1.5)
    ax.set_xticklabels([])
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.set_frame_on(False)  # Remove the borders
    ax.grid(False)  # Remove grid lines

create_density_plot(axs[0], spring_density)
create_density_plot(axs[1], summer_density)
create_density_plot(axs[2], winter_density)

plt.show()