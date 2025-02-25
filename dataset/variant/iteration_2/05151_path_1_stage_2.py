import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
lunar_rabbits_population = [50, 52, 58, 65, 70, 68, 75, 72, 71, 79, 80, 84]
sun_chameleons_population = [40, 42, 45, 48, 55, 53, 60, 58, 56, 62, 63, 67]

fig, ax = plt.subplots(figsize=(10, 6))

# Apply a single color consistently across all data groups
color = 'teal'
ax.plot(months, lunar_rabbits_population, marker='^', linestyle='-.', color=color, linewidth=2, markersize=8, label='Lunar Rabbits')
ax.plot(months, sun_chameleons_population, marker='D', linestyle=':', color=color, linewidth=2, markersize=8, label='Sun Chameleons')

# Annotate peak populations
ax.annotate(f'Peak: {max(lunar_rabbits_population)}', xy=(10, 79),
            xytext=(10.5, 74), arrowprops=dict(arrowstyle='->', color='darkgray'))
ax.annotate(f'Peak: {max(sun_chameleons_population)}', xy=(12, 67),
            xytext=(11, 71), arrowprops=dict(arrowstyle='->', color='darkgray'))

# Titles, labels
ax.set_title('Monthly Population Changes of Creatures\nIn a Fictional Ecosystem', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Population', fontsize=12)

# Grid style
ax.grid(True, linestyle='-', alpha=0.5, color='lightgray')

# Legend
ax.legend(loc='lower right', fontsize=12, shadow=True)

# Customized x-axis ticks
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45, ha='center')

plt.tight_layout()
plt.show()