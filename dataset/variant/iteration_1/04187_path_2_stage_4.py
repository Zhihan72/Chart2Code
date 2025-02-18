import matplotlib.pyplot as plt
import numpy as np

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
age_groups = ['Kids', 'Young Adults', 'Middle-aged', 'Seniors']

screen_time_0_12 = [5, 8, 12, 18, 25]
screen_time_19_35 = [10, 15, 25, 40, 50]
screen_time_36_55 = [8, 10, 15, 25, 30]
screen_time_56_plus = [5, 7, 10, 15, 20]

data = np.array([screen_time_0_12, screen_time_19_35, screen_time_36_55, screen_time_56_plus])

colors = ['#e6194b', '#ffe119', '#4363d8', '#f58231']

plt.figure(figsize=(12, 8))
plt.stackplot(decades, data, labels=age_groups, colors=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

plt.xlabel('Time Period', fontsize=12, labelpad=10)
plt.ylabel('Weekly Screen Hours', fontsize=12, labelpad=10)
plt.title('Screen Usage Trends by Generation', fontsize=16, fontweight='bold', pad=20)

plt.legend(title='Generations', loc='upper right', bbox_to_anchor=(0.9, 0.9), fontsize=10, shadow=True)
plt.xticks(rotation=30, ha='right')

plt.grid(axis='y', linestyle='--', linewidth=0.7, color='grey', alpha=0.6)

plt.tight_layout()
plt.show()