import matplotlib.pyplot as plt
import numpy as np

# Define the data for exotic tea consumption
consumption_percentages = [25, 20, 15, 25, 15]
colors = ['#6db33f', '#e07b39', '#9cc3d5', '#d58339', '#a34f4f']

# Define additional data for bar chart
years = ['2018', '2019', '2020', '2021', '2022']
# Hypothetical trend data for each tea over these years
trend_data = [
    [20, 22, 25, 28, 30],
    [18, 19, 21, 23, 20],
    [10, 12, 14, 15, 15],
    [22, 23, 24, 24, 25],
    [12, 14, 13, 15, 15]
]

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))

# Create the pie chart without text labels
wedges, _, autotexts = ax.pie(
    consumption_percentages, colors=colors,
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, 
    wedgeprops=dict(width=0.3), shadow=True, explode=(0.05,) * len(consumption_percentages)
)

# Customizing text properties
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

# Create secondary axes for overlaying a bar chart
ax2 = ax.twinx()

# Set up bar chart
x = np.arange(len(years))  # Position of bars
width = 0.15  # Width of each bar

# Plot bars for each tea type
for i, color in enumerate(colors):
    ax2.bar(x + i * width, trend_data[i], width, color=color, alpha=0.6)

# Customizing the overlay bar chart
ax2.set_xticks(x + width * 2)
ax2.set_xticklabels(years, fontsize=10)
ax2.set_ylim(0, 35)

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()