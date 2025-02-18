import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Minutes spent on different browsers each day
chrome_usage = [120, 130, 115, 125, 140, 180, 160]  # in minutes
firefox_usage = [60, 55, 70, 65, 50, 90, 85]  # in minutes
edge_usage = [20, 15, 10, 25, 30, 35, 20]  # in minutes

# Setting up the figure with 3 subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

# Titles for each subplot
titles = ["Chrome Usage", "Firefox Usage", "Edge Usage"]
usage_data = [chrome_usage, firefox_usage, edge_usage]
colors = ['#FF5733', '#FFC300', '#C70039']

# Plot histograms for the remaining browsers
for i, ax in enumerate(axes[:3]):
    ax.bar(days, usage_data[i], color=colors[i], edgecolor='black', alpha=0.7)
    ax.set_title(titles[i], fontsize=14, weight='bold')
    ax.set_ylabel("Minutes Spent", fontsize=12)
    ax.set_xlabel("Days of the Week", fontsize=12)
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Annotate each bar with the minutes spent
    for day, minutes in zip(days, usage_data[i]):
        ax.annotate(f'{minutes} min', xy=(day, minutes), xytext=(day, minutes + 5),
                    ha='center', fontsize=10, color='black')

# Set common x-tick labels and rotate them
for ax in axes[:3]:
    ax.set_xticks(days)
    ax.set_xticklabels(days, rotation=45, ha='right', fontsize=10)

# Main title for the entire figure
fig.suptitle('Daily Browser Usage Patterns of a Tech-Savvy Household\nMinutes Spent on Different Browsers Throughout the Week', 
             fontsize=16, fontweight='bold', y=1.02)

# Adjust layout to prevent overlap
fig.tight_layout()

# Display the plot
plt.show()