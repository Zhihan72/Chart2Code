import numpy as np
import matplotlib.pyplot as plt

# Define the days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Data representing average daily consumption of fruits and vegetables (in servings) for different age groups
kids = [3, 4, 3, 4, 4, 5, 6]
teens = [4, 5, 4, 5, 5, 6, 7]
adults = [5, 6, 5, 6, 6, 7, 8]
seniors = [4, 5, 5, 5, 6, 6, 7]

# Aggregate the data for easy plotting
data = np.array([kids, teens, adults, seniors])

# Additional related data for weekly averages
age_groups = ["Kids (0-12)", "Teens (13-17)", "Adults (18-64)", "Seniors (65+)"]
weekly_averages = [np.mean(kids), np.mean(teens), np.mean(adults), np.mean(seniors)]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Bar plot for weekly averages
axs[0].bar(age_groups, weekly_averages, color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])
axs[0].set_title("Weekly Average Intake of Fruits and Vegetables\nPer Age Group", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Age Groups", fontsize=14)
axs[0].set_ylabel("Average Servings Per Day", fontsize=14)
axs[0].set_ylim(0, 8)
axs[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Second subplot: Bar plot for daily consumption
bar_width = 0.2
x = np.arange(len(days))

# Plot each age group
axs[1].bar(x - bar_width*1.5, kids, width=bar_width, label='Kids (0-12)', color='#FF9999')
axs[1].bar(x - bar_width/2, teens, width=bar_width, label='Teens (13-17)', color='#66B3FF')
axs[1].bar(x + bar_width/2, adults, width=bar_width, label='Adults (18-64)', color='#99FF99')
axs[1].bar(x + bar_width*1.5, seniors, width=bar_width, label='Seniors (65+)', color='#FFCC99')

# Customize the bar plot
axs[1].set_title("Daily Intake of Fruits and Vegetables\nAcross Age Groups", fontsize=16, fontweight='bold')
axs[1].set_xlabel("Days of the Week", fontsize=14)
axs[1].set_ylabel("Average Servings", fontsize=14)
axs[1].set_xticks(x)
axs[1].set_xticklabels(days, rotation=45, fontsize=12)
axs[1].legend(title="Age Groups", fontsize=12, title_fontsize=14)
axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout for both subplots
plt.tight_layout()

# Display the plots
plt.show()