import matplotlib.pyplot as plt

volunteer_roles = ['Directors', 'IT Support', 'Chefs', 'Artists', 'Security', 'Coaches']
volunteer_counts = [15, 14, 18, 10, 8, 25]

# New color set
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(8, 8))
explode = (0, 0, 0, 0, 0.1, 0.1)

wedges, texts, autotexts = ax.pie(
    volunteer_counts,
    labels=volunteer_roles,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    shadow=False,
    wedgeprops=dict(width=0.3)  # Keeping the donut shape
)

for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('regular')

for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('navy')
    autotext.set_fontweight('bold')

ax.set_title(
    "Spring Fest Volunteer Roles",
    fontsize=16, fontweight='bold', pad=15
)

ax.legend(
    wedges, volunteer_roles,
    title="Roles",
    loc="upper right",
    bbox_to_anchor=(1, 0.7)
)

ax.grid(visible=True)

plt.show()