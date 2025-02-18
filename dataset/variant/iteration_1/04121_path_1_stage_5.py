import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data for densities in different seasons
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

autumn_density = np.array([
    [9, 13, 10, 12, 11], 
    [19, 22, 17, 20, 21], 
    [29, 34, 31, 27, 32],
    [24, 25, 27, 26, 23],
    [14, 15, 13, 12, 16]
])

# Create subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 20), tight_layout=True)

# Define colors for each seasonal plot
colors = ['darkorange', 'purple', 'teal', 'crimson']

# Helper function to plot
def create_horizontal_density_plot(ax, data, color):
    sns.violinplot(data=data, ax=ax, linewidth=1.5, orient='h', palette=[color]*data.shape[1])
    ax.set_xlabel('')
    ax.set_yticklabels([])
    ax.set_ylabel('')
    ax.set_title('')
    ax.set_frame_on(False)
    ax.grid(False)

# Shuffle the assigned colors and use them for each plot
create_horizontal_density_plot(axs[0], spring_density, colors[2])
create_horizontal_density_plot(axs[1], summer_density, colors[3])
create_horizontal_density_plot(axs[2], winter_density, colors[0])
create_horizontal_density_plot(axs[3], autumn_density, colors[1])

plt.show()