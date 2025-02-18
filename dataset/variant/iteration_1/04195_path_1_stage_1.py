import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2010, 2021)

# Randomly altered data for digital content consumption (in hours per week)
streaming_services = np.array([3, 6, 9, 14, 24, 36, 44, 56, 68, 71, 79])
podcasts = np.array([2, 1, 4, 6, 10, 9, 16, 20, 23, 24, 29])
ebooks = np.array([1, 3, 2, 5, 4, 8, 9, 11, 11, 14, 16])
online_magazines = np.array([4, 3, 5, 8, 8, 11, 11, 13, 14, 15, 16])

# Create a figure and adjust size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data using multiple line charts
ax.plot(years, streaming_services, label='Streaming Services', marker='o', color='#1f77b4')
ax.plot(years, podcasts, label='Podcasts', marker='o', color='#ff7f0e')
ax.plot(years, ebooks, label='E-Books', marker='o', color='#2ca02c')
ax.plot(years, online_magazines, label='Online Magazines', marker='o', color='#d62728')

# Annotate key points in trends (adjust based on new data)
ax.annotate('Boom in popularity', xy=(2016, 36), xytext=(2012, 41),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, color='black',
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

ax.annotate('Integrated media growth', xy=(2018, 13), xytext=(2014, 14),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, color='black',
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

# Set grid, title, and labels
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_title("Trends in Digital Content Consumption\n (2010-2020)", fontsize=16, pad=20)
ax.set_ylabel('Hours per Week', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.legend(loc='upper left', fontsize=10, title='Content Types')

# Rotate x-ticks for better readability
plt.xticks(rotation=45, ha='right')

# Add a tight layout
plt.tight_layout()

# Show the plot
plt.show()