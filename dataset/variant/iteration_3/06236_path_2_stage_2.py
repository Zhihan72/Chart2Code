import numpy as np
import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

kids = [3, 4, 3, 4, 4, 5, 6]
teens = [4, 5, 4, 5, 5, 6, 7]
adults = [5, 6, 5, 6, 6, 7, 8]
seniors = [4, 5, 5, 5, 6, 6, 7]

data = np.array([kids, teens, adults, seniors])

age_groups = ["Kids (0-12)", "Teens (13-17)", "Adults (18-64)", "Seniors (65+)"]
weekly_averages = [np.mean(kids), np.mean(teens), np.mean(adults), np.mean(seniors)]

fig, axs = plt.subplots(1, 2, figsize=(18, 8))

single_color = '#FF9999'  # Consistent color across all plots

axs[0].bar(age_groups, weekly_averages, color=single_color)
axs[0].set_title("Weekly Average Intake of Fruits and Vegetables\nPer Age Group", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Age Groups", fontsize=14)
axs[0].set_ylabel("Average Servings Per Day", fontsize=14)
axs[0].set_ylim(0, 8)
axs[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

bar_width = 0.2
x = np.arange(len(days))

axs[1].bar(x - bar_width*1.5, kids, width=bar_width, label='Kids (0-12)', color=single_color)
axs[1].bar(x - bar_width/2, teens, width=bar_width, label='Teens (13-17)', color=single_color)
axs[1].bar(x + bar_width/2, adults, width=bar_width, label='Adults (18-64)', color=single_color)
axs[1].bar(x + bar_width*1.5, seniors, width=bar_width, label='Seniors (65+)', color=single_color)

axs[1].set_title("Daily Intake of Fruits and Vegetables\nAcross Age Groups", fontsize=16, fontweight='bold')
axs[1].set_xlabel("Days of the Week", fontsize=14)
axs[1].set_ylabel("Average Servings", fontsize=14)
axs[1].set_xticks(x)
axs[1].set_xticklabels(days, rotation=45, fontsize=12)
axs[1].legend(title="Age Groups", fontsize=12, title_fontsize=14)
axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()