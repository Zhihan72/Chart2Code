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

def make_autopct(values):
    def custom_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{:.1f}%\n({:d})'.format(pct, val)
    return custom_autopct

# Adjusted plotting for a donut pie chart (ring)
fig, axs = plt.subplots(3, 2, figsize=(14, 10), subplot_kw=dict(aspect="equal"))
fig.suptitle('Social Media Usage Across Different Age Groups - Survey 2025', fontsize=16, fontweight='bold', y=1.05)

for ax, (group_name, data) in zip(axs.flatten(), data_by_age_group.items()):
    wedges, texts, autotexts = ax.pie(
        data, labels=platforms, autopct=make_autopct(data), startangle=140,
        colors=colors, pctdistance=0.85, wedgeprops=dict(edgecolor='w')
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    ax.set_title(f"Social Media\n{group_name}", fontsize=12, pad=10)
    ax.legend(wedges, platforms, title="Platforms", loc="best")

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()