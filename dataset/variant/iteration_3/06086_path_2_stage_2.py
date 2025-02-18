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

fig, axs = plt.subplots(3, 2, figsize=(14, 10), subplot_kw=dict(aspect="equal"))

for ax, (group_name, data) in zip(axs.flatten(), data_by_age_group.items()):
    wedges, texts, autotexts = ax.pie(
        data, labels=None, autopct=make_autopct(data), startangle=140,
        colors=colors, pctdistance=0.75, wedgeprops=dict(width=0.3, edgecolor='w')
    )

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()