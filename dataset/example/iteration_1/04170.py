import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This chart shows the daily temperature variations in three different fictional cities - Solaris, Rainfall, and Snowtown - over a week.
# The goal is to visualize how the temperatures fluctuate over a typical week, helping climatologists understand urban microclimates.

# Create data for the days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Temperature data for Solaris, Rainfall, and Snowtown
solar_temps = [30, 32, 31, 29, 28, 27, 26]  # Temperate city with moderate heat
rain_temps = [22, 24, 23, 21, 20, 19, 18]   # Cool and rainy city
snow_temps = [5, 6, 4, 3, 2, 1, 0]         # Snow-covered, cold city

# Convert days to a numerical range for better plotting
day_indices = np.arange(len(days))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the line charts
ax.plot(day_indices, solar_temps, marker='o', markersize=5, color='orange', label='Solaris', linestyle='-', linewidth=2)
ax.plot(day_indices, rain_temps, marker='o', markersize=5, color='blue', label='Rainfall', linestyle='-', linewidth=2)
ax.plot(day_indices, snow_temps, marker='o', markersize=5, color='purple', label='Snowtown', linestyle='-', linewidth=2)

# Adding title and labels
ax.set_title('Daily Temperature Variations in Fictional Cities\nSolaris, Rainfall & Snowtown', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Days of the Week', fontsize=12, weight='bold')
ax.set_ylabel('Temperature (°C)', fontsize=12, weight='bold')

# Setting custom ticks
ax.set_xticks(day_indices)
ax.set_xticklabels(days, rotation=45, ha='right')

# Adding grid for better readability
ax.grid(visible=True, linestyle='--', alpha=0.6)

# Adding a legend
ax.legend(loc='upper right', fontsize=11, shadow=True, title='Cities')

# Highlight specific days with vertical lines
highlight_days = [2, 5]  # Wednesday and Saturday
for day in highlight_days:
    ax.axvline(x=day, color='grey', linestyle='--', linewidth=1)

# Annotate significant points
ax.annotate('Midweek Peak\nin Solaris', xy=(2, 31), xytext=(3, 33),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')
ax.annotate('Weekend Drop\nin Snowtown', xy=(5, 1), xytext=(4, 3),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()