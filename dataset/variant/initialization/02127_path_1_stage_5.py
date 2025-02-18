import matplotlib.pyplot as plt

energy_sources = ['Power of the Sun', 'Breeze Energy', 'Water Might', 'Earth Heat']
energy_shares = [35, 30, 20, 15]
colors = ['#40E0D0', '#FFD700', '#ADFF2F', '#FF6347']
explode = (0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(9, 9))

# Create a pie chart with a white circle at the center to make it look like a donut
wedges, texts, autotexts = ax.pie(
    energy_shares, 
    labels=energy_sources, 
    autopct='%1.0f%%', 
    startangle=180, 
    colors=colors, 
    explode=explode,
    wedgeprops=dict(width=0.3)  # Add this line to make it a donut
)

for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color('black')

ax.set_title(
    'Renewable Energy Options - 2023', 
    fontsize=15, 
    fontweight='regular', 
    pad=20
)

ax.axis('equal')

plt.legend(
    wedges, energy_sources,
    title="Energy Types",
    loc="upper right",
    bbox_to_anchor=(0.5, 0.5, 0.5, 0.5),
    fontsize=11
)

plt.tight_layout()

plt.show()