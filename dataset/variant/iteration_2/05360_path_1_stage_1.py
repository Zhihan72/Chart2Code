import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Number of trees planted by each campaign (in thousands)
campaign_A = np.array([2, 3, 5, 7, 11, 13, 15, 20, 23, 30, 35])
campaign_B = np.array([1, 2, 3, 5, 8, 12, 17, 25, 31, 38, 45])
campaign_C = np.array([0, 1, 2, 4, 7, 10, 13, 18, 22, 29, 33])

# Calculate the cumulative number of trees planted for each campaign
cumulative_A = np.cumsum(campaign_A)
cumulative_B = np.cumsum(campaign_B)
cumulative_C = np.cumsum(campaign_C)

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Line plot for annual trees planted by each campaign (using a single color)
ax1.plot(years, campaign_A, marker='o', linestyle='-', color='purple', label='Campaign A', linewidth=2)
ax1.plot(years, campaign_B, marker='s', linestyle='-', color='purple', label='Campaign B', linewidth=2)
ax1.plot(years, campaign_C, marker='^', linestyle='-', color='purple', label='Campaign C', linewidth=2)

ax1.set_title('Annual Trees Planted by Different Campaigns in GreenVille (2010-2020)\nEfforts to Combat Urban Pollution', fontsize=16, fontweight='bold', pad=15)
ax1.set_ylabel('Trees Planted (Thousands)', fontsize=14)
ax1.legend(title='Campaigns', loc='upper left', fontsize=12, title_fontsize=13)
ax1.grid(True, linestyle='--', alpha=0.6)

# Line plot for cumulative trees planted by each campaign (using the same single color)
ax2.plot(years, cumulative_A, marker='o', linestyle='-', color='purple', label='Cumulative Campaign A', linewidth=2)
ax2.plot(years, cumulative_B, marker='s', linestyle='-', color='purple', label='Cumulative Campaign B', linewidth=2)
ax2.plot(years, cumulative_C, marker='^', linestyle='-', color='purple', label='Cumulative Campaign C', linewidth=2)

ax2.set_title('Cumulative Trees Planted by Each Campaign (2010-2020)', fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Cumulative Trees Planted (Thousands)', fontsize=14)
ax2.legend(title='Cumulative Campaigns', loc='upper left', fontsize=12, title_fontsize=13)
ax2.grid(True, linestyle='--', alpha=0.6)

# Annotate final values for cumulative trees planted
for year, value in zip(years, cumulative_A):
    ax2.annotate(f'{value}', xy=(year, value), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=9, color='purple')
for year, value in zip(years, cumulative_B):
    ax2.annotate(f'{value}', xy=(year, value), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=9, color='purple')
for year, value in zip(years, cumulative_C):
    ax2.annotate(f'{value}', xy=(year, value), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=9, color='purple')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()