import matplotlib.pyplot as plt

volunteer_roles = ['Organizers', 'Mentors', 'Caterers', 'Performers', 'Security', 'Technical Support']
volunteer_counts = [15, 25, 18, 10, 8, 14]

# Single color for all segments
single_color = ['#4682B4']  # Blue shade

fig, ax = plt.subplots(figsize=(10, 7))

# Explode first and fourth segments
explode = (0.1, 0, 0, 0.1, 0, 0)

# Plot pie chart with a single color applied to all
wedges, texts, autotexts = ax.pie(
    volunteer_counts,
    labels=volunteer_roles,
    colors=single_color * len(volunteer_roles),  # Repeat the single color for each segment
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True
)

for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax.set_title(
    "Volunteer Role Distribution for Annual Community Event",
    fontsize=14, fontweight='bold', pad=20
)

ax.legend(
    wedges, volunteer_roles,
    title="Volunteer Roles",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

plt.tight_layout()

plt.show()