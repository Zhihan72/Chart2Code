import matplotlib.pyplot as plt

# Altered volunteer roles and counts
volunteer_roles = ['Performers', 'Caterers', 'Organizers', 'Technical Support', 'Mentors', 'Security']
volunteer_counts = [10, 18, 15, 14, 25, 8]

single_color = ['#4682B4']

fig, ax = plt.subplots(figsize=(10, 7))

explode = (0.1, 0, 0.1, 0, 0, 0)

wedges, texts, autotexts = ax.pie(
    volunteer_counts,
    labels=volunteer_roles,
    colors=single_color * len(volunteer_roles),
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    shadow=True
)

for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax.set_title(
    "Volunteer Duties at the Gala",
    fontsize=16, fontweight='bold', pad=15
)

ax.legend(
    wedges, volunteer_roles,
    title="Roles",
    loc="upper left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

plt.tight_layout()

plt.show()