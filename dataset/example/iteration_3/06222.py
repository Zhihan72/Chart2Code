import matplotlib.pyplot as plt
import numpy as np

# Define the topic: Evolution of Social Media Engagement Over a Decade in Teenagers
years = np.arange(2011, 2021)

# Hypothetical data representing average daily time spent (in minutes) on different social media platforms
instagram = np.array([10, 15, 20, 25, 33, 45, 55, 60, 65, 70])
snapchat = np.array([0, 5, 12, 20, 25, 30, 40, 50, 55, 60])
facebook = np.array([20, 22, 24, 26, 28, 29, 30, 32, 34, 35])
twitter = np.array([10, 12, 15, 18, 22, 25, 27, 28, 30, 32])
tiktok = np.array([0, 0, 0, 0, 5, 15, 25, 35, 45, 55])

# Combine the data for the stackplot
data = np.vstack([instagram, snapchat, facebook, twitter, tiktok])

# Create a figure for the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, data, labels=['Instagram', 'Snapchat', 'Facebook', 'Twitter', 'TikTok'], 
             colors=['#c13584', '#FFFC00', '#3b5998', '#00aced', '#69C9D0'], alpha=0.8)

# Set title and labels
ax.set_title("Evolution of Social Media Engagement Among Teenagers (2011-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Average Daily Time Spent (minutes)", fontsize=14)

# Set x-ticks to avoid overlap and rotate them
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add grid and legend
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper left', title='Social Media Platforms', fontsize=10, bbox_to_anchor=(1.05, 1))

# Ensure the layout is adjusted for better readability
plt.tight_layout()

# Display the plot
plt.show()