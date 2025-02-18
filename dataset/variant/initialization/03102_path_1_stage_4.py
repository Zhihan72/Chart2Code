import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1980, 2025, 0.25)

def logistic_growth(t, L=100, k=0.1, x0=2000):
    return L / (1 + np.exp(-k * (t - x0)))

# Calculate usage data
email_usage = logistic_growth(years, x0=2010, L=90)
social_media_usage = logistic_growth(years, x0=2015, L=85)
video_conferencing_usage = logistic_growth(years, x0=2000, L=80)
messaging_apps_usage = logistic_growth(years, x0=2008, L=95)
mobile_apps_usage = logistic_growth(years, x0=2020, L=50)
iot_devices_usage = logistic_growth(years, x0=2010, L=100)

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot with various element styles
ax.stackplot(years, 
             email_usage, social_media_usage, video_conferencing_usage, messaging_apps_usage,
             mobile_apps_usage, iot_devices_usage,
             labels=['Email Usage', 'Social Media', 'Video Conferencing', 'Messaging Apps',
                     'Mobile Apps', 'IoT Devices'],
             colors=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8B4513', '#9400D3'], 
             alpha=0.8)

# Modify axis limits and ticks
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 500)

# Add grid lines with a different style
ax.grid(True, linestyle=':', linewidth=0.5, alpha=0.75)

# Rotate x-ticks
plt.xticks(np.arange(1980, 2025, 5), rotation=30)

# Adding a legend with a shadow and setting its location
ax.legend(loc='upper left', shadow=True, fontsize='small')

# Enhancing the borders
for spine in ax.spines.values():
    spine.set_color('gray')
    spine.set_linewidth(1.5)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()