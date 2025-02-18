import matplotlib.pyplot as plt

age_groups = ['Teens (13-19)', 'Young Adults (20-29)', 'Adults (30-45)', 'Middle-aged (46-60)', 'Seniors (61+)']
platforms = ['Instagram', 'Snapchat', 'Facebook', 'TikTok', 'Twitter']

data_by_age_group = {
    "Teens (13-19)": [20, 35, 25, 10, 10],  # Altered values
    "Young Adults (20-29)": [15, 30, 30, 15, 10],  # Altered values
    "Adults (30-45)": [10, 15, 45, 10, 20],  # Altered values
    "Middle-aged (46-60)": [5, 10, 65, 5, 15],  # Altered values
    "Seniors (61+)": [5, 10, 75, 5, 5]  # Altered values
}

colors = ['#ffad99', '#ff9999', '#66b3ff', '#ffcc99', '#99ff99']

fig, axs = plt.subplots(3, 2, figsize=(14, 10), subplot_kw=dict(aspect="equal"))
fig.suptitle('Social Media Usage Across Different Age Groups - Survey 2025', fontsize=16, fontweight='bold', y=1.05)

for ax, (group_name, data) in zip(axs.flatten(), data_by_age_group.items()):
    wedges, texts, autotexts = ax.pie(
        data, labels=platforms, autopct='%1.1f%%', startangle=90,
        colors=colors, pctdistance=0.90, wedgeprops=dict(edgecolor='gray', linestyle='--')
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc='lightgrey')
    ax.add_artist(centre_circle)
    ax.set_title(f"Social Media\n{group_name}", fontsize=12, pad=10)
    ax.grid(True, linestyle=':', color='lightblue')
    ax.legend(wedges, platforms, title="Platforms", loc="upper right", frameon=False)

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()