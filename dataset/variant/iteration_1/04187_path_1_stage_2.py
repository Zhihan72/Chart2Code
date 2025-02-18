import matplotlib.pyplot as plt
import numpy as np

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
age_groups = ['Kids', 'Teens', 'Young Adults', 'Middle-aged', 'Seniors']

# Preserved shuffled screen time data
screen_time_0_12 = [12, 18, 25, 5, 8]  
screen_time_13_18 = [45, 12, 8, 35, 20]  
screen_time_19_35 = [25, 40, 50, 15, 10]  
screen_time_36_55 = [15, 25, 8, 30, 10]  
screen_time_56_plus = [15, 10, 20, 5, 7]  

data = np.array([screen_time_0_12, screen_time_13_18, screen_time_19_35, screen_time_36_55, screen_time_56_plus])

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(12, 8))
plt.stackplot(decades, data, labels=age_groups, colors=colors, alpha=0.8)

plt.xlabel('Time Periods', fontsize=12)
plt.ylabel('Hours Weekly', fontsize=12)
plt.title('Screen Usage Patterns by Demographic Groups', fontsize=16, fontweight='bold', pad=20)
plt.legend(title='Demographics', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()