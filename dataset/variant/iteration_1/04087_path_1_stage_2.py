import matplotlib.pyplot as plt
import numpy as np

# Constructing contextual data for each age group
children_sleep = [9, 9.5, 10, 9, 9.5, 9, 10]
teenagers_sleep = [7.2, 8, 7.5, 8, 7.8, 7.5, 8.2]
adults_sleep = [6.5, 7, 6.8, 7, 6.9, 7, 6.5]
seniors_sleep = [6, 6.5, 6.2, 6.5, 6.7, 6.5, 6.3]

# Combine data into a list
data = [children_sleep, teenagers_sleep, adults_sleep, seniors_sleep]

# Initialize the figure
fig, axs = plt.subplots(1, 1, figsize=(12, 8))

# Violin Plot
violin = axs.violinplot(data, vert=True, showmeans=True, showextrema=True, showmedians=True)

# Customizing the plot
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
for i, pc in enumerate(violin['bodies']):
    pc.set_facecolor(colors[i % len(colors)])
    pc.set_edgecolor('black')
    pc.set_alpha(0.6)

# Customizing the mean, medians, and extrema lines:
violin['cmeans'].set_color('blue')
violin['cmedians'].set_color('green')
for partname in ('cbars', 'cmins', 'cmaxes'):
    vp = violin[partname]
    vp.set_edgecolor('black')
    vp.set_linewidth(1)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()