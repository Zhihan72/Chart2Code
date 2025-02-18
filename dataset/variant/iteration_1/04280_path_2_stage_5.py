import matplotlib.pyplot as plt

volunteer_roles = ['Performers', 'Caterers', 'Organizers', 'Technical Support', 'Mentors', 'Security']
volunteer_counts = [10, 18, 15, 14, 25, 8]
colors = ['#FF6347', '#6A5ACD', '#32CD32', '#FFD700', '#FF1493', '#008080']

fig, ax = plt.subplots(figsize=(10, 7))

explode = (0.1, 0, 0.1, 0, 0, 0) 

# Setting the 'wedgeprops' to have a width creating a donut chart.
wedges, texts, autotexts = ax.pie(
    volunteer_counts,
    labels=volunteer_roles,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    wedgeprops=dict(width=0.3),
    shadow=False
)

for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('black')
    autotext.set_fontweight('bold')

ax.set_title(
    "Gala Volunteer Roles Distribution",
    fontsize=14, fontweight='normal', pad=20
)

ax.legend(
    wedges, volunteer_roles,
    title="Volunteer Roles",
    loc="upper right",
    bbox_to_anchor=(1, 0, 0.5, 1),
    frameon=False
)

plt.tight_layout()
plt.grid(True)

plt.show()