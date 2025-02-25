import matplotlib.pyplot as plt
import numpy as np

# Age groups and their respective hours of sleep per night
age_groups = ['Kids', 'Teens', 'Adults', 'Seniors']
child_sleep = [10, 11, 9, 10, 8.5, 9, 10.5, 11, 12, 8]
teen_sleep = [7, 8, 7.5, 7, 6.5, 8, 9, 7, 6, 8.5]
adult_sleep = [6, 6.5, 7, 5.5, 7.5, 6, 7, 8, 6, 5]
senior_sleep = [5.5, 6, 6.5, 5, 6, 7, 5.5, 6, 5, 6]

all_sleep_data = child_sleep + teen_sleep + adult_sleep + senior_sleep

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

bins = np.linspace(4.5, 12, 15)
ax1.hist([child_sleep, teen_sleep, adult_sleep, senior_sleep], 
         bins=bins, label=age_groups, rwidth=0.9)

ax1.set_title('Sleep Hours by Age', fontsize=14, fontweight='bold')
ax1.set_xlabel('Sleep Hours', fontsize=12)
ax1.set_ylabel('Count', fontsize=12)
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.5, linestyle='--')

colors = ['skyblue', 'lightcoral', 'lightgreen', 'orchid']
for i, (data, color) in enumerate(zip([child_sleep, teen_sleep, adult_sleep, senior_sleep], colors)):
    ax2.hist(data, bins=bins, alpha=0.6, label=age_groups[i], color=color, edgecolor='black')

ax2.set_title('Age Group Sleep Patterns', fontsize=14, fontweight='bold')
ax2.set_xlabel('Sleep Hours', fontsize=12)
ax2.set_ylabel('Count', fontsize=12)
ax2.legend(loc='upper right')

ax1.annotate('Optimal (7-9 hrs)', xy=(8, 8), xytext=(9.5, 6),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', facecolor='black'), 
             fontsize=10, bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

ax2.annotate('Seniors < 7 hrs', xy=(5.5, 3), xytext=(7, 2),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', facecolor='black'), 
             fontsize=10, bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

plt.tight_layout()
plt.show()