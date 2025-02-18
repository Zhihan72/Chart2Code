import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2013, 2024)

# Artificial data for digital media consumption (in millions) per year for each category
video_streaming = [50, 65, 80, 95, 115, 135, 160, 190, 220, 250, 280]
music_streaming = [30, 35, 40, 50, 60, 75, 95, 115, 135, 160, 180]
podcasts = [5, 8, 12, 18, 25, 33, 43, 55, 70, 85, 100]

# Combine datasets for the stackplot without E-books
media_types = np.array([video_streaming, music_streaming, podcasts])

# Create the area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot stackplot without E-books
ax.stackplot(years, media_types, labels=['Video Streaming', 'Music Streaming', 'Podcasts'],
             colors=['skyblue', 'limegreen', 'coral'], alpha=0.8)

# Set title, labels, and legend
ax.set_title("Evolution of Digital Media Consumption in TechTropolis\n(2013-2023)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Consumption (Millions of Users)", fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Media Type', fontsize=10)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Rotate x-axis labels to prevent overlap
plt.xticks(rotation=45)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()