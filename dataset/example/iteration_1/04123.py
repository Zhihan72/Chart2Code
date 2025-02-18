import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are planning a harmonic music festival where numerous bands from various genres will perform at different times of the day. 
# Let's visualize the number of bands performing throughout the day, and for added context, let's include another subplot showing the average audience attendance at those times.

# Define times of the day
times = np.array(['08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'])

# Number of bands performing at the designated times 
pop_bands = np.array([2, 3, 5, 7, 9, 10, 8, 6])
rock_bands = np.array([1, 2, 4, 3, 6, 8, 7, 5])
indie_bands = np.array([0, 1, 2, 4, 3, 5, 6, 4])

# Audience attendance at those times in hundreds
audience_attendance = np.array([5, 8, 15, 25, 35, 45, 40, 30])

# Setting up the figure with two subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 12), sharex=True)

# Plotting number of bands performing over time
axes[0].plot(times, pop_bands, '-o', label='Pop Bands', color='magenta')
axes[0].plot(times, rock_bands, '-s', label='Rock Bands', color='blue')
axes[0].plot(times, indie_bands, '-^', label='Indie Bands', color='green')

# Adding titles and labels to the band performance chart
axes[0].set_title('Number of Bands Performing Throughout the Day', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Number of Bands', fontsize=12)
axes[0].legend(loc='upper left', fontsize=10)
axes[0].grid(alpha=0.3, linestyle='--', linewidth=0.7)

# Plotting audience attendance
axes[1].plot(times, audience_attendance, '-D', label='Audience Attending (x100)', color='orange')

# Adding titles and labels to the audience attendance chart
axes[1].set_title('Audience Attendance Throughout the Day', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Time of Day', fontsize=12)
axes[1].set_ylabel('Audience (x100)', fontsize=12)
axes[1].legend(loc='upper left', fontsize=10)
axes[1].grid(alpha=0.3, linestyle='--', linewidth=0.7)

# Adjust x-axis labels to prevent overlap
for ax in axes:
    ax.tick_params(axis='x', rotation=45)

# Optimize layout
plt.tight_layout()

# Display the plots
plt.show()