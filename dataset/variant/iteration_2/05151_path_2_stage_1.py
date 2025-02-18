import matplotlib.pyplot as plt
import numpy as np

# Define time (in months) and randomly altered population data of Lunar Rabbits and Sun Chameleons
months = np.arange(1, 13)
lunar_rabbits_population = [70, 68, 52, 65, 79, 71, 50, 72, 71, 84, 80, 75]  # Altered values
sun_chameleons_population = [58, 42, 48, 40, 63, 60, 55, 45, 62, 56, 53, 67]  # Altered values

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
ax.plot(months, lunar_rabbits_population, marker='o', linestyle='-', color='darkorange', linewidth=2, markersize=6, label='Lunar Rabbits')
ax.plot(months, sun_chameleons_population, marker='s', linestyle='--', color='teal', linewidth=2, markersize=6, label='Sun Chameleons')

# Highlight the peak points in the populations
max_lunar_population = max(lunar_rabbits_population)
max_lunar_month = months[lunar_rabbits_population.index(max_lunar_population)]
max_sun_population = max(sun_chameleons_population)
max_sun_month = months[sun_chameleons_population.index(max_sun_population)]

# Annotate the peak populations
ax.annotate(f'Peak: {max_lunar_population}', xy=(max_lunar_month, max_lunar_population),
            xytext=(max_lunar_month + 0.5, max_lunar_population - 5),
            arrowprops=dict(arrowstyle='->', color='gray'))

ax.annotate(f'Peak: {max_sun_population}', xy=(max_sun_month, max_sun_population),
            xytext=(max_sun_month + 0.5, max_sun_population + 5),
            arrowprops=dict(arrowstyle='->', color='gray'))

# Add titles and labels
ax.set_title('Monthly Population Changes of Lunar Rabbits and Sun Chameleons\nIn a Fictional Ecosystem', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Population', fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper left', fontsize=10)

# Customize the x-axis ticks
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45, ha='right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()