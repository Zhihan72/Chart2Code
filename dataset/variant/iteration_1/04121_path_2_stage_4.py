import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define the locations
locations = ['Zone 1', 'Zone 2', 'Sector 3', 'Area 4', 'Field 5']

# Activity data scaled (measurements per km²) for five phases
phase_one_activity = np.array([
    [10, 15, 11, 14, 12], 
    [20, 23, 18, 21, 22], 
    [30, 35, 32, 28, 33],
    [25, 26, 28, 27, 24],
    [15, 16, 14, 13, 17]
])

phase_two_activity = np.array([
    [12, 18, 13, 16, 14], 
    [22, 25, 20, 23, 24], 
    [32, 37, 34, 30, 35],
    [27, 28, 30, 29, 26],
    [17, 18, 16, 15, 19]
])

phase_three_activity = np.array([
    [8, 12, 9, 11, 10], 
    [18, 21, 16, 19, 20], 
    [28, 33, 30, 26, 31],
    [23, 24, 26, 25, 22],
    [13, 14, 12, 11, 15]
])

phase_four_activity = np.array([
    [13, 17, 14, 15, 16], 
    [25, 28, 22, 27, 29], 
    [35, 38, 33, 31, 36],
    [29, 30, 32, 31, 28],
    [19, 21, 18, 17, 20]
])

phase_five_activity = np.array([
    [11, 14, 12, 13, 13], 
    [23, 26, 21, 24, 25], 
    [33, 36, 31, 29, 34],
    [26, 27, 29, 28, 25],
    [16, 17, 15, 14, 18]
])

# Create figure with subplots for five phases
fig, axs = plt.subplots(5, 1, figsize=(10, 25), tight_layout=True)

def create_density_plot(ax, data, phase):
    for i, loc in enumerate(locations):
        sns.kdeplot(data[:, i], ax=ax, label=loc, fill=True)
    ax.set_title(f'Animal Activity Density - {phase}', fontsize=14, fontweight='bold')
    ax.set_ylabel('Density', fontsize=12)
    ax.set_xlabel('Activity (measurements per km²)', fontsize=12)
    ax.legend(handles=ax.get_legend(), labels=locations, title='Location', fontsize=10)
    ax.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Create density plots for each phase
create_density_plot(axs[0], phase_one_activity, 'Phase One')
create_density_plot(axs[1], phase_two_activity, 'Phase Two')
create_density_plot(axs[2], phase_three_activity, 'Phase Three')
create_density_plot(axs[3], phase_four_activity, 'Phase Four')
create_density_plot(axs[4], phase_five_activity, 'Phase Five')

plt.show()