import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart aims to illustrate the average monthly rainfall in a fictional region called Rainforestia
# over the span of one year across its four unique seasons: Spring, Summer, Autumn, and Winter.

# Define months and corresponding average rainfall (in millimeters)
months = np.arange(1, 13)
rainfall = np.array([85, 78, 92, 110, 134, 158, 102, 75, 65, 45, 40, 70])

# Define seasons
seasons = ["Winter", "Spring", "Summer", "Autumn"]
season_colors = ['skyblue', 'lightgreen', 'gold', 'coral']
season_labels = [("Winter", 0, 1), ("Spring", 2, 4), ("Summer", 5, 7), ("Autumn", 8, 10)]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot bar chart for average monthly rainfall
bars = ax.bar(months, rainfall, color=[season_colors[(month - 1) // 3] for month in months], edgecolor='black')

# Annotate each bar with the rainfall amount
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), textcoords='offset points', ha='center', fontsize=10, color='black')

# Add titles and labels
ax.set_title("Average Monthly Rainfall in Rainforestia\n(One Year Period)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Average Rainfall (mm)", fontsize=14)

# Customize x-ticks with month names
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticks(months)
ax.set_xticklabels(month_labels, fontsize=12)

# Add gridlines
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Add legend for seasons
handles = [plt.Rectangle((0, 0), 1, 1, color=season_colors[i], edgecolor='black') for i in range(4)]
ax.legend(handles, seasons, title="Season", title_fontsize=12, fontsize=10, loc='upper right')

# Highlight important insights with annotations
ax.annotate('Rainiest Month', xy=(5, rainfall[4]), xytext=(6, 150),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='darkblue')
ax.annotate('Dry Spell', xy=(9.5, rainfall[10]), xytext=(8, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='darkred')

# Highlight months by seasons using vspan
for season, start, end in season_labels:
    ax.axvspan(months[start] - 0.5, months[end + 1] - 0.5, color=season_colors[(start // 3)], alpha=0.1)

# Automatically adjust layout before displaying
plt.tight_layout()

# Display the plot
plt.show()