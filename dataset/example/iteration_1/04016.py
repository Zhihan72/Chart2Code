import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of the daily browser usage patterns of a tech-savvy household. 
# Data includes the number of minutes spent on different browsers throughout the day for one week.

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Minutes spent on different browsers each day (manually crafted data)
chrome_usage = [120, 130, 115, 125, 140, 180, 160]  # in minutes
firefox_usage = [60, 55, 70, 65, 50, 90, 85]  # in minutes
safari_usage = [30, 25, 20, 35, 40, 50, 45]  # in minutes
edge_usage = [20, 15, 10, 25, 30, 35, 20]  # in minutes

# Constructing the data array
browser_data = np.array([chrome_usage, firefox_usage, safari_usage, edge_usage])

# Setting up the figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Titles for each subplot
titles = ["Chrome Usage", "Firefox Usage", "Safari Usage", "Edge Usage"]
usage_data = [chrome_usage, firefox_usage, safari_usage, edge_usage]
colors = ['#FF5733', '#FFC300', '#DAF7A6', '#C70039']

# Plotting histograms for each browser
for i, ax in enumerate(axes):
    ax.bar(days, usage_data[i], color=colors[i], edgecolor='black', alpha=0.7)
    ax.set_title(titles[i], fontsize=14, weight='bold')
    ax.set_ylabel("Minutes Spent", fontsize=12)
    ax.set_xlabel("Days of the Week", fontsize=12)
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Annotating each bar with the minutes spent
    for day, minutes in zip(days, usage_data[i]):
        ax.annotate(f'{minutes} min', xy=(day, minutes), xytext=(day, minutes + 5),
                    ha='center', fontsize=10, color='black')

# Setting common x-tick labels and rotating them
for ax in axes:
    ax.set_xticks(days)
    ax.set_xticklabels(days, rotation=45, ha='right', fontsize=10)

# Main title for the entire figure
fig.suptitle('Daily Browser Usage Patterns of a Tech-Savvy Household\nMinutes Spent on Different Browsers Throughout the Week', 
             fontsize=16, fontweight='bold', y=1.02)

# Adjusting layout to prevent overlap
fig.tight_layout()

# Displaying the plot
plt.show()