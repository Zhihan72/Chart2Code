import matplotlib.pyplot as plt
import numpy as np

# Data - Years and Shuffled Popularity Scores (out of 100)
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
netflix_popularity = np.array([82, 88, 78, 92, 95, 85, 97, 93, 96])  # Shuffled
amazon_prime_popularity = np.array([65, 55, 70, 58, 62, 75, 87, 80, 85])  # Shuffled
hulu_popularity = np.array([50, 56, 58, 60, 64, 53, 66, 62, 68])  # Shuffled
disney_plus_popularity = np.array([0, 45, 0, 0, 0, 60, 90, 75, 85])  # Shuffled

# Plotting the line chart
plt.figure(figsize=(12, 8))

# Plot each platform's popularity trend with shuffled colors
plt.plot(years, netflix_popularity, marker='o', linestyle='-', color='green', label='Netflix')  # Changed from red to green
plt.plot(years, amazon_prime_popularity, marker='s', linestyle='-', color='purple', label='Amazon Prime')  # Changed from blue to purple
plt.plot(years, hulu_popularity, marker='^', linestyle='-', color='red', label='Hulu')  # Changed from green to red
plt.plot(years, disney_plus_popularity, marker='d', linestyle='-', color='blue', label='Disney+')  # Changed from purple to blue

# Title and Labels
plt.title("Popularity Trends of Streaming Platforms (2015-2023)\nHow the Market Has Evolved Over Years", fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Score (out of 100)', fontsize=12)

# Adding legend and customized grid
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Annotate significant events
plt.annotate('Disney+ Launch', xy=(2019.5, 45), xytext=(2017, 55),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center')

# Ensures layout is adjusted to fit elements within the figure
plt.tight_layout()

# Show the plot
plt.show()