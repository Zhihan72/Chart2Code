import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
lunar_rabbits_population = [70, 68, 52, 65, 79, 71, 50, 72, 71, 84, 80, 75]
sun_chameleons_population = [58, 42, 48, 40, 63, 60, 55, 45, 62, 56, 53, 67]

fig, ax = plt.subplots(figsize=(10, 6))

# Swapped colors: teal for Lunar Rabbits and darkorange for Sun Chameleons
ax.plot(months, lunar_rabbits_population, marker='o', linestyle='-', color='teal', linewidth=2, markersize=6, label='Lunar Rabbits')
ax.plot(months, sun_chameleons_population, marker='s', linestyle='--', color='darkorange', linewidth=2, markersize=6, label='Sun Chameleons')

max_lunar_population = max(lunar_rabbits_population)
max_lunar_month = months[lunar_rabbits_population.index(max_lunar_population)]
max_sun_population = max(sun_chameleons_population)
max_sun_month = months[sun_chameleons_population.index(max_sun_population)]

ax.annotate(f'Peak: {max_lunar_population}', xy=(max_lunar_month, max_lunar_population),
            xytext=(max_lunar_month + 0.5, max_lunar_population - 5),
            arrowprops=dict(arrowstyle='->', color='gray'))

ax.annotate(f'Peak: {max_sun_population}', xy=(max_sun_month, max_sun_population),
            xytext=(max_sun_month + 0.5, max_sun_population + 5),
            arrowprops=dict(arrowstyle='->', color='gray'))

ax.set_title('Monthly Population Changes of Lunar Rabbits and Sun Chameleons\nIn a Fictional Ecosystem', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Population', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', fontsize=10)
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45, ha='right')
plt.tight_layout()
plt.show()