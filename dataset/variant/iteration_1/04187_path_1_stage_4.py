import matplotlib.pyplot as plt
import numpy as np

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
age_groups = ['Kids', 'Teens', 'Young Adults', 'Middle-aged', 'Seniors']

screen_time_0_12 = [12, 18, 25, 5, 8]  
screen_time_13_18 = [45, 12, 8, 35, 20]  
screen_time_19_35 = [25, 40, 50, 15, 10]  
screen_time_36_55 = [15, 25, 8, 30, 10]  
screen_time_56_plus = [15, 10, 20, 5, 7]  

data = np.array([screen_time_0_12, screen_time_13_18, screen_time_19_35, screen_time_36_55, screen_time_56_plus])

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(10, 6))
plt.stackplot(decades, data, labels=age_groups, colors=colors, alpha=0.7)

plt.xlabel('Time Periods', fontsize=11)
plt.ylabel('Weekly Hours', fontsize=11)
plt.title('Screen Usage Patterns by Demographic Groups', fontsize=15, fontweight='bold', pad=15)

plt.legend(title='Demographic Groups', loc='upper left', bbox_to_anchor=(1, 1), fontsize=9)
plt.xticks(rotation=40, ha='right', fontsize=9)
plt.yticks(fontsize=9)

plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)

plt.tight_layout()
plt.show()