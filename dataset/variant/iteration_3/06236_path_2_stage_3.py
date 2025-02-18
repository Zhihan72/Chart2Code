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

# Calculate overall mean
overall_mean = np.mean(weekly_averages)

# Diverging bar chart for weekly averages (subplot 0)
diverging_values = np.array(weekly_averages) - overall_mean
axs[0].barh(age_groups, diverging_values, color=['#FF6666' if v < 0 else '#66B3FF' for v in diverging_values])
axs[0].axvline(0, color='black', linewidth=0.8)
axs[0].set_title("Deviation from Overall Average Intake\nPer Age Group", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Deviation from Mean Servings Per Day", fontsize=14)
axs[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Diverging bar chart for daily data (subplot 1)
x = np.arange(len(days))
means = data.mean(axis=0)
diverging_data = data - means

for i, (age_group, d_data) in enumerate(zip(age_groups, diverging_data)):
    axs[1].bar(x, d_data, label=age_group, bottom=diverging_data[:i].sum(axis=0),
               color=['#FF6666' if v < 0 else '#66B3FF' for v in d_data])

axs[1].axhline(0, color='black', linewidth=0.8)
axs[1].set_title("Daily Deviation from Mean Intake\nAcross Age Groups", fontsize=16, fontweight='bold')
axs[1].set_xlabel("Days of the Week", fontsize=14)
axs[1].set_ylabel("Deviation from Mean Servings", fontsize=14)
axs[1].set_xticks(x)
axs[1].set_xticklabels(days, rotation=45, fontsize=12)
axs[1].legend(title="Age Groups", fontsize=12, title_fontsize=14)
axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()