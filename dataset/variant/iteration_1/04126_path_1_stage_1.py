import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Fictional data representing hours spent weekly on different digital media
# Data is altered while preserving original dimensional structure
streaming_services = np.array([12, 17, 22, 28, 35, 42, 50, 2, 3, 5, 8])  # Random alteration within the group
social_media = np.array([22, 25, 30, 34, 38, 4, 6, 9, 11, 14, 18])
online_news = np.array([11, 14, 16, 19, 21, 23, 25, 3, 5, 7, 9])
podcasts = np.array([8, 9, 11, 13, 15, 1, 2, 3, 4, 5, 6])

# Stack the data for the area chart
media_data = np.vstack([streaming_services, social_media, online_news, podcasts])

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, media_data, labels=['Streaming Services', 'Social Media', 'Online News', 'Podcasts'], 
             colors=['#1e90ff', '#ff6347', '#32cd32', '#8a2be2'], alpha=0.8)

# Set labels and title
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Weekly Hours Spent on Digital Media', fontsize=14)
ax.set_title("Exploring the Growth of Digital Media Consumption (2010-2020)", fontsize=18, fontweight='bold')

# Customize the x-axis to show every year
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Adding grid lines for better readability
ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# Add legend outside of plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Digital Media')

# Annotate significant developments
ax.annotate('Streaming Booms', xy=(2018, 42), xytext=(2016, 50),  # Adjusted position due to new data
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

ax.annotate('Podcasts Rise', xy=(2020, 58), xytext=(2018, 65),  # Adjusted position due to new data
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Adjust layout to ensure proper spacing
plt.tight_layout()

# Display the plot
plt.show()