import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the trends in digital content consumption over a decade (2010-2020). 
# We compare the consumption of Streaming Services, Podcasts, E-Books, and Online Magazines.

# Define years
years = np.arange(2010, 2021)

# Create data for digital content consumption (in hours per week)
streaming_services = np.array([2, 5, 10, 15, 25, 35, 45, 55, 65, 70, 80])
podcasts = np.array([1, 2, 3, 5, 7, 10, 15, 18, 22, 25, 28])
ebooks = np.array([1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 15])
online_magazines = np.array([3, 4, 6, 7, 9, 10, 12, 12, 13, 14, 15])

# Create a figure and adjust size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data using multiple line charts
ax.plot(years, streaming_services, label='Streaming Services', marker='o', color='#1f77b4')
ax.plot(years, podcasts, label='Podcasts', marker='o', color='#ff7f0e')
ax.plot(years, ebooks, label='E-Books', marker='o', color='#2ca02c')
ax.plot(years, online_magazines, label='Online Magazines', marker='o', color='#d62728')

# Annotate key points in trends
ax.annotate('Boom in popularity', xy=(2016, 35), xytext=(2012, 40),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, color='black',
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

ax.annotate('Integrated media growth', xy=(2018, 12), xytext=(2014, 13),
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

# Add a tight layout to automatically adjust the plots
plt.tight_layout()

# Show the plot
plt.show()