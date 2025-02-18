import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart demonstrates the trend of international space missions over the last decade, showcasing the number of successful missions by major spacefaring nations.
# Title: "A Decade of International Space Missions Success (2010-2020)"

# Data: Number of successful space missions by year for three major spacefaring nations: USA, Russia, and China.
years = np.arange(2010, 2021)
usa_missions = np.array([15, 16, 18, 21, 22, 27, 30, 32, 33, 35, 37])
russia_missions = np.array([25, 24, 22, 20, 22, 23, 25, 24, 27, 28, 30])
china_missions = np.array([5, 6, 8, 10, 12, 15, 18, 20, 23, 25, 28])

# Calculate total space missions per year
total_missions = usa_missions + russia_missions + china_missions

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Lines for each country's missions
ax1.plot(years, usa_missions, label='USA', marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)
ax1.plot(years, russia_missions, label='Russia', marker='d', linestyle='--', color='red', linewidth=2, markersize=8)
ax1.plot(years, china_missions, label='China', marker='s', linestyle='-.', color='green', linewidth=2, markersize=8)

# Twin axis for total missions overlay
ax2 = ax1.twinx()
ax2.plot(years, total_missions, label='Total Missions', color='purple', linestyle='-', marker='v', linewidth=3, markersize=10, alpha=0.6)

# Titles and labels
ax1.set_title("A Decade of International Space Missions Success (2010-2020)", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Number of Successful Missions", fontsize=14)
ax2.set_ylabel("Total Missions", fontsize=14)

# Adding grid for readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Annotating significant years and missions 
annotations = {
    2015: 'USA surpasses 20 missions',
    2018: 'China reaches 20 missions',
    2020: 'Total missions peak'
}

for year, text in annotations.items():
    ax1.annotate(text, (year, total_missions[year - 2010]),
                xytext=(5, 30), textcoords='offset points',
                arrowprops=dict(arrowstyle='->', color='black'),
                ha='center', fontsize=10, color='brown')

# Legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

# Ensure all years are marked on the x-axis
ax1.set_xticks(years)

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()