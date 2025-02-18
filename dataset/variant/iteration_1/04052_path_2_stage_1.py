import matplotlib.pyplot as plt
import numpy as np

# Data representing the subscription counts for four sports from 2000 to 2020
years = np.arange(2000, 2021)
soccer_subs = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180]
basketball_subs = [30, 32, 35, 38, 42, 45, 48, 50, 55, 60, 65, 70, 75, 80, 85, 90, 100, 110, 120, 130, 140]
tennis_subs = [20, 22, 24, 26, 28, 30, 32, 35, 38, 40, 45, 50, 55, 58, 60, 62, 65, 70, 75, 80, 85]
esports_subs = [5, 10, 15, 20, 28, 35, 40, 50, 60, 70, 85, 100, 115, 130, 145, 160, 175, 190, 210, 230, 250]

# Creating the figure and Subplots
fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# Plotting multiple line plots
ax.plot(years, soccer_subs, marker='o', linestyle='-', linewidth=2, color='#1f77b4')
ax.plot(years, basketball_subs, marker='x', linestyle='--', linewidth=2, color='#ff7f0e')
ax.plot(years, tennis_subs, marker='s', linestyle='-.', linewidth=2, color='#2ca02c')
ax.plot(years, esports_subs, marker='^', linestyle=':', linewidth=2, color='#d62728')

# Adding Chart Titles and Labels
ax.set_title('The Rise in Popularity of Various Sports (2000-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, fontweight='semibold')
ax.set_ylabel('Subscribers (in Thousands)', fontsize=14, fontweight='semibold')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()