import matplotlib.pyplot as plt

# Age groups and their social media preferences (percentage)
age_groups = ['Teens (13-19)', 'Young Adults (20-29)', 'Adults (30-45)', 'Middle-aged (46-60)', 'Seniors (61+)']
platforms = ['Instagram', 'Snapchat', 'Facebook', 'TikTok', 'Twitter']

data_by_age_group = {
    "Teens (13-19)": [25, 30, 20, 15, 10],
    "Young Adults (20-29)": [20, 25, 25, 20, 10],
    "Adults (30-45)": [15, 10, 40, 15, 20],
    "Middle-aged (46-60)": [10, 5, 60, 10, 15],
    "Seniors (61+)": [5, 5, 80, 5, 5]
}

colors = ['#ffad99', '#ff9999', '#66b3ff', '#ffcc99', '#99ff99']

fig, axs = plt.subplots(3, 2, figsize=(14, 10), subplot_kw=dict(aspect="equal"))
fig.suptitle('Social Media Usage Across Different Age Groups - Survey 2025', fontsize=16, fontweight='bold', y=1.05)

for ax, (group_name, data) in zip(axs.flatten(), data_by_age_group.items()):
    wedges, texts, autotexts = ax.pie(
        data, labels=platforms, autopct='%1.1f%%', startangle=90,  # Changed start angle for variation
        colors=colors, pctdistance=0.90, wedgeprops=dict(edgecolor='gray', linestyle='--')  # Changed edge color and line style
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc='lightgrey')  # Changed center circle color
    ax.add_artist(centre_circle)
    ax.set_title(f"Social Media\n{group_name}", fontsize=12, pad=10)
    ax.grid(True, linestyle=':', color='lightblue')  # Added grid with different style
    ax.legend(wedges, platforms, title="Platforms", loc="upper right", frameon=False)  # Changed legend location and removed frame

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()