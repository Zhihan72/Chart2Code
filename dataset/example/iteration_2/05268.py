import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2013 to 2022
years = np.arange(2013, 2023)

# Data for user growth in millions
socialgram_users = [
    50, 75, 110, 150, 200, 260, 330, 410, 500, 600,
]

chatbuzz_users = [
    60, 80, 100, 130, 170, 220, 280, 350, 430, 520,
]

imageshare_users = [
    30, 45, 70, 100, 140, 190, 250, 320, 400, 490,
]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each platform's user data
ax.plot(years, socialgram_users, label='SocialGram', marker='o', linestyle='-', linewidth=2.5, color='blue', alpha=0.7)
ax.plot(years, chatbuzz_users, label='ChatBuzz', marker='s', linestyle='-', linewidth=2.5, color='green', alpha=0.7)
ax.plot(years, imageshare_users, label='ImageShare', marker='^', linestyle='-', linewidth=2.5, color='orange', alpha=0.7)

# Set labels and title with line breaks for readability
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Users (Millions)', fontsize=12)
ax.set_title('User Growth Trends of Major Social Media Platforms (2013-2022)', fontsize=16, fontweight='bold')

# Customize ticks for better spacing and readability
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 800, 100))

# Add grid for visual clarity
ax.grid(True, linestyle='--', alpha=0.6)

# Remove unnecessary plot spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a legend to help identify the data series
ax.legend(loc='upper left', fontsize=11)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()