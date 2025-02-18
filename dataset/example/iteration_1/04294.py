import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the world of sports, technology has been playing a crucial role in improving athlete performance. The hypothetical study measures
# the Performance Improvement Index (PII) of athletes in different sports over two decades, highlighting the influence of wearable technology.
# This chart provides insights on how PII has evolved from 2000 to 2020 across various sports, showing the impact of technology in enhancing performance.

# Define the years and the Performance Improvement Index for various sports
years = np.arange(2000, 2021)
football_pii = [50 + 3*np.sin(0.2*x) + 2*x for x in range(len(years))]
basketball_pii = [45 + 2.5*np.cos(0.15*x) + 2.1*x for x in range(len(years))]
tennis_pii = [48 + 2.8*np.sin(0.18*x + np.pi/6) + 1.8*x for x in range(len(years))]
athletics_pii = [55 + 3.2*np.sin(0.2*x) + 2.5*x for x in range(len(years))]
cycling_pii = [40 + 3.5*np.cos(0.2*x + np.pi/4) + 2.3*x for x in range(len(years))]

# Create the plot
fig, ax = plt.subplots(figsize=(16, 9))

# Plotting the line chart for different sports
ax.plot(years, football_pii, marker='o', linestyle='-', linewidth=2, color='navy', label='Football')
ax.plot(years, basketball_pii, marker='s', linestyle='--', linewidth=2, color='crimson', label='Basketball')
ax.plot(years, tennis_pii, marker='^', linestyle='-.', linewidth=2, color='green', label='Tennis')
ax.plot(years, athletics_pii, marker='d', linestyle=':', linewidth=2, color='purple', label='Athletics')
ax.plot(years, cycling_pii, marker='p', linestyle='-', linewidth=2, color='orange', label='Cycling')

# Title and labels
ax.set_title('Impact of Wearable Technology on Athlete Performance\nPerformance Improvement Index (PII) from 2000 to 2020', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Performance Improvement Index (PII)', fontsize=15)

# Adding a legend
ax.legend(title='Sports', loc='upper left', fontsize=12)

# Annotate for notable points
ax.annotate('Rapid Advancements in Tech', xy=(2015, football_pii[15]), xytext=(2008, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
ax.annotate('Tech Integration Peak', xy=(2018, athletics_pii[18]), xytext=(2011, 100),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Grid and styling
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f0f0f0')

# Automatically adjust layout 
plt.tight_layout()

# Display the plot
plt.show()