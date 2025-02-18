import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.array([2017, 2018, 2019, 2020, 2021])

# Activities in the park (Number of participants)
running = np.array([150, 175, 200, 180, 220])
cycling = np.array([100, 120, 130, 110, 140])
picnicking = np.array([80, 85, 95, 90, 100])
swimming = np.array([60, 75, 80, 60, 85])
yoga = np.array([30, 40, 50, 45, 60])

# Calculate total participation per year
total_participation = running + cycling + picnicking + swimming + yoga

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot stacked bar chart
activities = [running, cycling, picnicking, swimming, yoga]
colors = ['#2ca02c', '#d62728', '#9467bd', '#1f77b4', '#ff7f0e']

bottom = np.zeros(len(years))

for activity, color in zip(activities, colors):
    ax1.bar(years, activity, bottom=bottom, color=color, alpha=0.85, edgecolor='black')
    bottom += activity

# Create a secondary axis for total participation line plot
ax2 = ax1.twinx()
ax2.plot(years, total_participation, color='grey', marker='s', linestyle='--', linewidth=2)

# Customize ticks
ax1.set_xticks(years)
ax1.set_xticklabels([])  # Remove group labels
ax1.set_yticks([])       # Remove axis labels

# Remove secondary y-axis labels
ax2.set_yticks([])

# Remove tight layout adjustment for space conservation
plt.tight_layout(rect=[0, 0, 1, 1])

# Show plot
plt.show()