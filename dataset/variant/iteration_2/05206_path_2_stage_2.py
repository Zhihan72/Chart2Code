import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2013, 2021)
facebook_hours = [1.5, 1.7, 2.0, 2.3, 2.5, 2.8, 3.0, 3.1]
instagram_hours = [0.5, 0.7, 1.0, 1.5, 2.0, 2.3, 2.6, 2.8]
twitter_hours = [0.8, 1.0, 1.1, 1.4, 1.6, 1.7, 1.9, 2.0]

# Creating the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting data with shuffled colors
ax.plot(years, facebook_hours, color='green', linestyle='-', marker='o')  # Changed from 'blue'
ax.plot(years, instagram_hours, color='blue', linestyle='--', marker='s')  # Changed from 'purple'
ax.plot(years, twitter_hours, color='purple', linestyle='-.', marker='^')  # Changed from 'green'

# Customizing appearance
ax.grid(True, linestyle='--', alpha=0.6)

# Display the plot
plt.show()