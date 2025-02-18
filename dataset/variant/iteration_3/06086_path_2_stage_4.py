import matplotlib.pyplot as plt

age_groups = ['Teens (13-19)', 'Young Adults (20-29)', 'Adults (30-45)', 'Middle-aged (46-60)', 'Seniors (61+)']
platforms = ['Instagram', 'Snapchat', 'Facebook', 'TikTok', 'Twitter']

# Manually altered data for each age group (sum of percentages still totals 100)
data_by_age_group = {
    "Teens (13-19)": [20, 10, 15, 25, 30],
    "Young Adults (20-29)": [25, 20, 20, 10, 25],
    "Adults (30-45)": [20, 40, 10, 15, 15],
    "Middle-aged (46-60)": [15, 10, 5, 60, 10],
    "Seniors (61+)": [5, 80, 5, 5, 5]
}

# Shuffled color list
colors = ['#ff9999', '#99ff99', '#ffad99', '#66b3ff', '#ffcc99']

def make_autopct(values):
    def custom_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{:.1f}%\n({:d})'.format(pct, val)
    return custom_autopct

fig, axs = plt.subplots(3, 2, figsize=(14, 10), subplot_kw=dict(aspect="equal"))

for ax, (group_name, data) in zip(axs.flatten(), data_by_age_group.items()):
    wedges, texts, autotexts = ax.pie(
        data, labels=None, autopct=make_autopct(data), startangle=140,
        colors=colors, pctdistance=0.75, wedgeprops=dict(width=0.3, edgecolor='w')
    )

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()