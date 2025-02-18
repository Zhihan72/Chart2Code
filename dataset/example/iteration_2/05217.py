import matplotlib.pyplot as plt
import numpy as np

# Backstory: Examining the sleeping habits of people across different age groups for a sleep health study

# Age groups and their respective hours of sleep per night (contextual data)
age_groups = ['Children (5-12)', 'Teens (13-19)', 'Adults (20-64)', 'Seniors (65+)']
child_sleep = [10, 11, 9, 10, 8.5, 9, 10.5, 11, 12, 8]
teen_sleep = [7, 8, 7.5, 7, 6.5, 8, 9, 7, 6, 8.5]
adult_sleep = [6, 6.5, 7, 5.5, 7.5, 6, 7, 8, 6, 5]
senior_sleep = [5.5, 6, 6.5, 5, 6, 7, 5.5, 6, 5, 6]

# Combine data for histogram
all_sleep_data = child_sleep + teen_sleep + adult_sleep + senior_sleep

# Setting up the figure and subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Plotting histogram for individual age groups' sleep data combined
bins = np.linspace(4.5, 12, 15)
ax1.hist([child_sleep, teen_sleep, adult_sleep, senior_sleep], 
         bins=bins, label=age_groups, rwidth=0.9)

ax1.set_title('Distribution of Sleep Hours Across Different Age Groups', fontsize=14, fontweight='bold')
ax1.set_xlabel('Hours of Sleep per Night', fontsize=12)
ax1.set_ylabel('Frequency', fontsize=12)
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.5, linestyle='--')

# Plotting individual histograms for each age group
colors = ['skyblue', 'lightcoral', 'lightgreen', 'orchid']
for i, (data, color) in enumerate(zip([child_sleep, teen_sleep, adult_sleep, senior_sleep], colors)):
    ax2.hist(data, bins=bins, alpha=0.6, label=age_groups[i], color=color, edgecolor='black')

ax2.set_title('Sleep Patterns by Age Group', fontsize=14, fontweight='bold')
ax2.set_xlabel('Hours of Sleep per Night', fontsize=12)
ax2.set_ylabel('Frequency', fontsize=12)
ax2.legend(loc='upper right')

# Adding annotation for insights
ax1.annotate('Optimal Sleep\nRange (7-9 hours)', xy=(8, 8), xytext=(9.5, 6),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', facecolor='black'), 
             fontsize=10, bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

ax2.annotate('Most Seniors Sleep \nLess than 7 hours', xy=(5.5, 3), xytext=(7, 2),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', facecolor='black'), 
             fontsize=10, bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

# Automatically adjust layout
plt.tight_layout()
plt.show()