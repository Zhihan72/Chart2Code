import matplotlib.pyplot as plt

volunteer_roles = ['Mentors', 'Performers', 'Security', 'Caterers', 'Technical Support', 'Organizers']
volunteer_counts = [25, 10, 8, 18, 14, 15]

single_color = ['#4682B4']

fig, ax = plt.subplots(figsize=(10, 7))

explode = (0, 0.1, 0, 0, 0.1, 0)

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