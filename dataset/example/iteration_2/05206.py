import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart depicts the evolution of three popular social media platforms' usage hours per day over a span of eight years (2013-2020).
# These platforms are Facebook, Instagram, and Twitter.
# We provide explicit data for each of the platforms and differentiate line styles to enhance visibility.

# Data setup
years = np.arange(2013, 2021)
facebook_hours = [1.5, 1.7, 2.0, 2.3, 2.5, 2.8, 3.0, 3.1]
instagram_hours = [0.5, 0.7, 1.0, 1.5, 2.0, 2.3, 2.6, 2.8]
twitter_hours = [0.8, 1.0, 1.1, 1.4, 1.6, 1.7, 1.9, 2.0]

# Creating the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting data
ax.plot(years, facebook_hours, label='Facebook', color='blue', linestyle='-', marker='o')
ax.plot(years, instagram_hours, label='Instagram', color='purple', linestyle='--', marker='s')
ax.plot(years, twitter_hours, label='Twitter', color='green', linestyle='-.', marker='^')

# Adding annotations
ax.annotate('Instagram surpasses 1 hour mark', xy=(2016, 1.5), xytext=(2017, 2),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')
ax.annotate('Facebook reaches 3 hours', xy=(2018, 3), xytext=(2017, 2.6),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Customizing appearance
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Daily Usage (hours)', fontsize=12)
ax.set_title('Average Daily Social Media Usage Hours\n(2013-2020)', fontsize=16, fontweight='bold')

# Enhancing the grid
ax.grid(True, linestyle='--', alpha=0.6)

# Setting xticks and labels
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Adding legend
ax.legend(title='Platform', loc='upper left', fontsize=10, frameon=False)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()