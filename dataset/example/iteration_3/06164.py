import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The script showcases the consumption and calories information about various fruits 
# in a local community nutrition survey conducted in 2023. The goal is to visualize 
# the average consumption and the total calories intake from different fruits.

# Fruits and their data
fruits = ['Apples', 'Bananas', 'Oranges', 'Strawberries', 'Grapes']
consumption_data = [50, 30, 40, 20, 10]        # Average number of servings per month
calories_data = [2000, 1500, 1600, 500, 300]   # Total calories from the consumption

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Set positions for the bars
x_pos = np.arange(len(fruits))
bar_width = 0.4

# Plotting the bar chart for the consumption data
bars1 = ax1.bar(x_pos, consumption_data, width=bar_width, color='#6A5ACD', label='Consumption (Servings)', alpha=0.7)

# Setting up a secondary y-axis for the calories data
ax2 = ax1.twinx()
bars2 = ax2.bar(x_pos + bar_width, calories_data, width=bar_width, color='#FF6347', label='Total Calories', alpha=0.7)

# Add data labels on top of the bars for consumption
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=10, color='blue')

# Add data labels on top of the bars for calories
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center', va='bottom', fontsize=10, color='red')

# Titles and labels
plt.title('Fruits Consumption and Caloric Intake\nCommunity Nutrition Survey 2023', fontsize=16, fontweight='bold')
ax1.set_xlabel('Fruits', fontsize=12)
ax1.set_ylabel('Average Consumption (Servings)', fontsize=12, color='#6A5ACD')
ax2.set_ylabel('Total Calories', fontsize=12, color='#FF6347')

# Customize x-axis with fruit names
ax1.set_xticks(x_pos + bar_width / 2)
ax1.set_xticklabels(fruits, fontsize=12, rotation=45, ha='right')

# Adding legends
bars = [bars1[0], bars2[0]]
legends = [bars1.get_label(), bars2.get_label()]
ax1.legend(bars, legends, loc='upper left')

# Enhancing y-axis visibility with grid lines
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()