import matplotlib.pyplot as plt

# Constructing contextual data for each age group
children_sleep = [9, 9.5, 10, 9, 9.5, 9, 10]
teenagers_sleep = [7.2, 8, 7.5, 8, 7.8, 7.5, 8.2]
young_adults_sleep = [7, 7.5, 7.3, 7.8, 7.5, 7.4, 7.6]
adults_sleep = [6.5, 7, 6.8, 7, 6.9, 7, 6.5]
middle_aged_sleep = [6.7, 7, 6.8, 6.9, 7, 7.1, 6.8]
seniors_sleep = [6, 6.5, 6.2, 6.5, 6.7, 6.5, 6.3]

# Combine data into a list
data = [children_sleep, teenagers_sleep, young_adults_sleep, adults_sleep, middle_aged_sleep, seniors_sleep]

# Initialize the figure
fig, axs = plt.subplots(1, 1, figsize=(12, 8))

# Violin Plot
violin = axs.violinplot(data, vert=True, showmeans=True, showextrema=True, showmedians=True)

# Customizing the plot with new colors
new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4']
for i, pc in enumerate(violin['bodies']):
    pc.set_facecolor(new_colors[i % len(new_colors)])
    pc.set_edgecolor('black')
    pc.set_alpha(0.6)

# Customizing the mean, medians, and extrema lines
violin['cmeans'].set_color('blue')
violin['cmedians'].set_color('green')
for partname in ('cbars', 'cmins', 'cmaxes'):
    vp = violin[partname]
    vp.set_edgecolor('black')
    vp.set_linewidth(1)

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()