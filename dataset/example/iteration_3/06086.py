import matplotlib.pyplot as plt

# Backstory: A survey was conducted on social media usage across different age groups in the year 2025.
# The results show how prevalent each social media platform is in each age group.

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

# Color palette for each platform
colors = ['#ffad99', '#ff9999', '#66b3ff', '#ffcc99', '#99ff99']

# Helper function to create custom labels for pie chart
def make_autopct(values):
    def custom_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{:.1f}%\n({:d})'.format(pct, val)
    return custom_autopct

# Create a function to generate individual pies for each age group
def plot_social_media_pie(data, group_name, platforms, colors):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

    wedges, texts, autotexts = ax.pie(
        data, labels=platforms, autopct=make_autopct(data), startangle=140,
        colors=colors, pctdistance=0.85, wedgeprops=dict(edgecolor='w'),
        textprops=dict(size=10)
    )

    # Add a white circle at the center to create a donut effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)

    # Title for each subplot
    ax.set_title(f"Social Media Usage\n{group_name}", fontsize=12, pad=20)
    
    # Add a legend to each subplot
    ax.legend(wedges, platforms, title="Platforms", loc="best")

    # Annotate wedges with custom labels and arrows
    for i, autotext in enumerate(autotexts):
        autotext.set_color('white')
        autotext.set_fontsize(8)
        autotext.set_fontweight('bold')
        
    plt.tight_layout()

# Plotting all age groups in a single figure with multiple subplots
fig, axs = plt.subplots(3, 2, figsize=(14, 10), subplot_kw=dict(aspect="equal"))
fig.suptitle('Social Media Usage Across Different Age Groups - Survey 2025', fontsize=16, fontweight='bold', y=1.05)

for ax, (group_name, data) in zip(axs.flatten(), data_by_age_group.items()):
    wedges, texts, autotexts = ax.pie(
        data, labels=platforms, autopct=make_autopct(data), startangle=140,
        colors=colors, pctdistance=0.85, wedgeprops=dict(edgecolor='w'),
        textprops=dict(size=8)
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    ax.set_title(f"Social Media\n{group_name}", fontsize=12, pad=10)
    ax.legend(wedges, platforms, title="Platforms", loc="best")

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()