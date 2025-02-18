import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define the regions
regions = ['Region A', 'Region B', 'Region C', 'Region D', 'Region E']

# Bird sightings data (density per km²) for three periods
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

# Create a figure with multiple subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 15), tight_layout=True)

# Define the density plot function without titles and labels
def create_density_plot(ax, data):
    sns.violinplot(data=data, ax=ax, linewidth=1.5)
    ax.set_xticklabels([])  # Remove the region labels
    ax.set_xlabel('')  # Remove the x axis label
    ax.set_ylabel('')  # Remove the y axis label
    ax.set_title('')  # Remove the title

# Create density plots for each season
create_density_plot(axs[0], spring_density)
create_density_plot(axs[1], summer_density)
create_density_plot(axs[2], winter_density)

# Show the plot
plt.show()