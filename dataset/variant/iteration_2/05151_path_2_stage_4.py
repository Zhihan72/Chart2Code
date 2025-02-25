import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
lunar_rabbits_population = [70, 68, 52, 65, 79, 71, 50, 72, 71, 84, 80, 75]
sun_chameleons_population = [58, 42, 48, 40, 63, 60, 55, 45, 62, 56, 53, 67]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(months, lunar_rabbits_population, marker='D', linestyle='-.', color='navy', linewidth=1.5, markersize=7, label='Blue Moon Hares')
ax.plot(months, sun_chameleons_population, marker='x', linestyle=':', color='crimson', linewidth=1.5, markersize=7, label='Solar Iguanas')

max_lunar_population = max(lunar_rabbits_population)
max_lunar_month = months[lunar_rabbits_population.index(max_lunar_population)]
max_sun_population = max(sun_chameleons_population)
max_sun_month = months[sun_chameleons_population.index(max_sun_population)]

ax.annotate(f'Apex: {max_lunar_population}', xy=(max_lunar_month, max_lunar_population),
            xytext=(max_lunar_month + 0.5, max_lunar_population - 5),
            arrowprops=dict(arrowstyle='->', color='black'))

ax.annotate(f'Apex: {max_sun_population}', xy=(max_sun_month, max_sun_population),
            xytext=(max_sun_month + 0.5, max_sun_population + 5),
            arrowprops=dict(arrowstyle='->', color='black'))

ax.set_title('Yearly Wild Numbers of Blue Moon Hares and Solar Iguanas\nIn an Imaginary Habitat', fontsize=14, fontweight='bold')
ax.set_xlabel('Time Cycle', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.grid(True, linestyle='-', alpha=0.5)
ax.legend(loc='lower right', fontsize=10)
ax.set_xticks(months)
ax.set_xticklabels(['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven'], rotation=45, ha='right')
plt.tight_layout()
plt.show()