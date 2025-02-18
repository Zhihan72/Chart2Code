import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Altered Study: Observational Study on Animal Activity Patterns
# Focus: Comparing Activity Levels in Diverse Areas During Distinct Phases

# Define the locations
locations = ['Zone 1', 'Zone 2', 'Sector 3', 'Area 4', 'Field 5']

# Activity data scaled (measurements per km²) for three phases
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

# Create figure with subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 15), tight_layout=True)

# Define the plot function
def create_activity_plot(ax, data, phase):
    sns.violinplot(data=data,
                   ax=ax, linewidth=1.5)
    ax.set_title(f'Animal Activity Levels in Various Locations - {phase}', fontsize=14, fontweight='bold')
    ax.set_xlabel('Location', fontsize=12)
    ax.set_ylabel('Activity (measurements per km²)', fontsize=12)
    ax.set_xticklabels(locations, rotation=30, ha='right')

# Create plots for each phase
create_activity_plot(axs[0], phase_one_activity, 'Phase One')
create_activity_plot(axs[1], phase_two_activity, 'Phase Two')
create_activity_plot(axs[2], phase_three_activity, 'Phase Three')

# Show the plot
plt.show()