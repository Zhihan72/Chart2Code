import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are analyzing the trend of average daily step counts for three different age groups
# over the course of a week. This helps in understanding how physical activity varies among 
# children, adults, and elderly across a typical week.

# Days of the week
days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

# Average steps per day for three different age groups
children_steps = np.array([15000, 16000, 15500, 15000, 14800, 17000, 18000])
adults_steps = np.array([10000, 10500, 10200, 9800, 9500, 11000, 11500])
elderly_steps = np.array([7000, 7200, 7100, 7000, 6800, 7300, 7500])

# Create the figure and the axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot lines for each age group with distinct styles
ax.plot(days, children_steps, marker='o', linestyle='-', linewidth=2, label='Children (5-12 years)', color='#FF5733')
ax.plot(days, adults_steps, marker='s', linestyle='--', linewidth=2, label='Adults (20-40 years)', color='#33FF57')
ax.plot(days, elderly_steps, marker='^', linestyle='-.', linewidth=2, label='Elderly (65+ years)', color='#3357FF')

# Title and labels
ax.set_title("Daily Step Count Trend: A Comparison Across Age Groups", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Day of the Week", fontsize=14)
ax.set_ylabel("Average Steps per Day", fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate peak days
peak_children = np.max(children_steps)
peak_adults = np.max(adults_steps)
peak_elderly = np.max(elderly_steps)

ax.annotate('Peak Day', xy=('Sun', peak_children), xytext=('Sat', peak_children + 1000),
            arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='darkred')
ax.annotate('Peak Day', xy=('Sun', peak_adults), xytext=('Sat', peak_adults + 500),
            arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='darkgreen')
ax.annotate('Peak Day', xy=('Sun', peak_elderly), xytext=('Sat', peak_elderly + 500),
            arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='darkblue')

# Add legend
ax.legend(title='Age Group', fontsize=10, loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()