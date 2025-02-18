import matplotlib.pyplot as plt

age_groups = ['Teen Faction (13-19)', 'Young Souls (20-29)', 'Mature People (30-45)', 'Mid Lifers (46-60)', 'Wise Ones (61+)']
platforms = ['Insta', 'Snap', 'FB', 'Tikky', 'Tweetie']

data_by_age_group = {
    "Teen Faction (13-19)": [20, 35, 25, 10, 10],
    "Young Souls (20-29)": [15, 30, 30, 15, 10],
    "Mature People (30-45)": [10, 15, 45, 10, 20],
    "Mid Lifers (46-60)": [5, 10, 65, 5, 15],
    "Wise Ones (61+)": [5, 10, 75, 5, 5]
}

# Define a single color to be used consistently across all pies for all slices
consistent_color = '#66b3ff'

fig, axs = plt.subplots(3, 2, figsize=(14, 10), subplot_kw=dict(aspect="equal"))
fig.suptitle('Digital Social Interaction per Age Group - Observation 2025', fontsize=16, fontweight='bold', y=1.05)

for ax, (group_name, data) in zip(axs.flatten(), data_by_age_group.items()):
    wedges, texts, autotexts = ax.pie(
        data, labels=platforms, autopct='%1.1f%%', startangle=90,
        colors=[consistent_color]*len(data), pctdistance=0.90, wedgeprops=dict(edgecolor='gray', linestyle='--')
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc='lightgrey')
    ax.add_artist(centre_circle)
    ax.set_title(f"Platforms of Choice\n{group_name}", fontsize=12, pad=10)
    ax.grid(True, linestyle=':', color='lightblue')
    ax.legend(wedges, platforms, title="Network", loc="upper right", frameon=False)

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()