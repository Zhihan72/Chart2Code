import matplotlib.pyplot as plt
import numpy as np

# Backstory: A comparative study on the amount of sleep (in hours) athletes from different sports get during their training periods.
# Data: Sleep hours for athletes in Basketball, Football, Swimming, Running, and Cycling. 

# Constructing the data
basketball_sleep_hours = [7.5, 8, 8.1, 7.9, 8.3, 8, 7.8, 8.2, 8.3, 8.1, 7.9, 8, 7.5, 8, 8.2, 8.4, 8.6, 7.8, 8.1, 7.9]
football_sleep_hours = [8.5, 8.1, 7.9, 8, 8.4, 8.2, 7.8, 8.1, 8.2, 8.3, 8.5, 8.4, 8.3, 8.1, 8.6, 8.7, 8.5, 8.3, 8.2, 8.4]
swimming_sleep_hours = [7.8, 7.5, 7.9, 8, 8.1, 8.3, 8.4, 7.9, 8, 7.7, 7.8, 8.2, 8, 7.9, 8.1, 8.5, 7.9, 8, 7.6, 8.1]
running_sleep_hours = [7.2, 7.5, 7.8, 7.7, 7.9, 7.6, 7.8, 7.6, 7.5, 7.7, 7.9, 8, 7.6, 7.8, 7.7, 8.1, 7.9, 7.5, 7.8, 7.6]
cycling_sleep_hours = [8.3, 8.1, 7.9, 8.4, 8.2, 8.6, 8.1, 8.3, 8.2, 8.7, 8.5, 8.3, 8.4, 8.2, 8.6, 8.1, 8.5, 8.3, 8.7, 8.2]

# Combining the data into a list of lists
sleep_hours_data = [basketball_sleep_hours, football_sleep_hours, swimming_sleep_hours, running_sleep_hours, cycling_sleep_hours]

# Sport names
sports = ['Basketball', 'Football', 'Swimming', 'Running', 'Cycling']

# Create the box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Box plot characteristics
box = ax.boxplot(sleep_hours_data, patch_artist=True,
                 notch=True,
                 boxprops=dict(facecolor='lightblue', color='navy'),
                 whiskerprops=dict(color='navy'),
                 capprops=dict(color='navy'),
                 flierprops=dict(marker='o', color='red', markersize=8, alpha=0.6),
                 medianprops=dict(color='darkorange', linewidth=2))

# Colors for the boxes
colors = ['#C1E1C1', '#A1C3D1', '#FFB347', '#FF6961', '#FFB6C1']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Adding a horizontal strip plot overlay for better data distribution visualization
for i, sport_data in enumerate(sleep_hours_data, start=1):
    plt.scatter(np.full_like(sport_data, i), sport_data, alpha=0.6, edgecolor='k', linewidth=0.5)

# Set title and labels
ax.set_title('Athlete Sleep Patterns During Training:\nHours of Sleep Per Night by Sport', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Sleep Hours per Night', fontsize=12)
ax.set_xticklabels(sports, fontsize=11, fontweight='bold')

# Add grid lines for readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adding observed means as points
means = [np.mean(sport_data) for sport_data in sleep_hours_data]
plt.scatter(range(1, len(sports) + 1), means, color='blue', marker='D', label='Mean')

# Customizing appearance of whiskers, caps, and medians
plt.setp(box['whiskers'], color='grey', linestyle='-.')
plt.setp(box['caps'], color='grey')
plt.setp(box['medians'], color='black')

# Adding legend
plt.legend(['Data Points', 'Mean'], loc='upper right')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()