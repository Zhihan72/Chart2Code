import matplotlib.pyplot as plt
import numpy as np

# Updated data with an additional exotic tea type
tea_types = ['Matcha (Japan)', 'Masala Chai (India)', 'Moroccan Mint (Morocco)', 
             'Rooibos (South Africa)', 'Hibiscus (Central America)', 'Yerba Mate (Argentina)']
consumption_percentages = [20, 20, 15, 20, 15, 10]
colors = ['#6db33f', '#e07b39', '#9cc3d5', '#d58339', '#a34f4f', '#8B4513']

# Extended trend data for the new tea type
years = ['2018', '2019', '2020', '2021', '2022']
trend_data = {
    'Matcha (Japan)': [20, 22, 25, 28, 30],
    'Masala Chai (India)': [18, 19, 21, 23, 20],
    'Moroccan Mint (Morocco)': [10, 12, 14, 15, 15],
    'Rooibos (South Africa)': [22, 23, 24, 24, 25],
    'Hibiscus (Central America)': [12, 14, 13, 15, 15],
    'Yerba Mate (Argentina)': [8, 10, 12, 11, 10]
}

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))

# Pie chart
wedges, texts, autotexts = ax.pie(
    consumption_percentages, labels=tea_types, colors=colors,
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, 
    wedgeprops=dict(width=0.3), shadow=True, explode=(0.05,) * len(tea_types)
)

# Customizing text properties
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
for text in texts:
    text.set_fontsize(11)

# Adding a legend
ax.legend(wedges, tea_types, title="Tea Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Secondary axes for overlaying a bar chart
ax2 = ax.twinx()

# Set up bar chart
x = np.arange(len(years))  # Position of bars
width = 0.13  # Adjusted for additional bar

# Plot bars for each tea type
for i, tea in enumerate(tea_types):
    ax2.bar(x + i * width, trend_data[tea], width, label=tea, color=colors[i], alpha=0.6)

# Customizing the overlay bar chart
ax2.set_ylabel('Annual Consumption Trend (%)', fontsize=12)
ax2.set_xticks(x + width * (len(tea_types) - 1) / 2)
ax2.set_xticklabels(years, fontsize=10)
ax2.set_ylim(0, 35)
ax2.legend(title="Yearly Trends", loc="upper left", bbox_to_anchor=(1.05, 1))

# Customize the plot title
plt.title("The World of Exotic Teas:\nA Global Consumption Snapshot and Yearly Trends", 
          fontsize=14, fontweight='bold', pad=20)

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()