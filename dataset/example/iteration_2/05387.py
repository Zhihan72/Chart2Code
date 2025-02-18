import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are going to visualize data on the monthly production output of different types of renewable energy 
# sources (Solar, Wind, Hydro, Geothermal) over a year. This data aims to highlight the variability 
# in monthly production outputs for each energy source.

# Artificial Data for Monthly Production Outputs in Megawatt-hours (MWh)
# Data is presented without using randomness and is deliberately varied
solar = [450, 520, 495, 530, 600, 680, 750, 720, 640, 580, 540, 500]
wind = [350, 380, 410, 480, 520, 570, 620, 590, 530, 490, 450, 410]
hydro = [700, 690, 720, 750, 800, 850, 900, 870, 830, 790, 750, 710]
geothermal = [310, 300, 320, 330, 350, 360, 380, 370, 350, 340, 320, 310]

# Combine data into a list for the box plot
data = [solar, wind, hydro, geothermal]
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal']

# Set up colors for each box
colors = ['#f9a825', '#1e88e5', '#81c784', '#ff7043']

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot a horizontal boxplot with customized colors and styles
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=False, whis=1.5,
                boxprops=dict(facecolor='lightgray', color='black', linewidth=1.5),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2),
                flierprops=dict(marker='o', color='black', alpha=0.5))

# Set individual colors for each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Annotate the mean value for each energy source in the box plot
means = [np.mean(source) for source in data]
for mean, y_pos in zip(means, range(1, len(data) + 1)):
    ax.plot(mean, y_pos, 'D', markerfacecolor='cyan', markersize=8, label='Mean' if y_pos == 1 else "")
    # Annotate the exact mean value
    ax.annotate(f'{mean:.1f} MWh', xy=(mean, y_pos), xytext=(mean + 20, y_pos),
                verticalalignment='center', fontsize=9, color='darkblue')

# Set the title and labels with breaks for improved readability
ax.set_title('Renewable Energy Production Insights:\nMonthly Output Variability Across Different Sources (2022)', fontsize=16, pad=20)
ax.set_xlabel('Monthly Production Output (MWh)', fontsize=12)
ax.set_ylabel('Energy Source', fontsize=12)

# Set the y-ticks and labels
ax.set_yticks(np.arange(1, len(energy_sources) + 1))
ax.set_yticklabels(energy_sources, fontsize=10)

# Highlight total output per energy source
for i, source in enumerate(data):
    total_output = sum(source)
    ax.annotate(f'Total: {total_output} MWh', xy=(max(source) + 20, i + 1),
                xytext=(max(source) + 20, i + 1), fontsize=9, color='green')

# Customize grid for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Make layout adjustments to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()