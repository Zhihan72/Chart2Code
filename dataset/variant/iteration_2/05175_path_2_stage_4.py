import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydro', 'Geo', 'Nuc', 'Bio']
energy_percentages = [40, 30, 12, 8, 6, 4]
colors = ['#1E90FF', '#00CED1', '#8B4513', '#FFD700', '#9400D3', '#FF4500']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect='equal'))

# Random selection: Explode Hydro
explode = (0, 0, 0.1, 0, 0, 0)  
# Random selection: Change wedgeprops and add linestyle dashdot
wedges, texts, autotexts = ax.pie(
    energy_percentages,
    explode=explode,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=100,  # Random startangle
    colors=colors,
    wedgeprops=dict(edgecolor='gray', linewidth=3, linestyle='dashdot', width=0.5),
    shadow=False  # Removing shadow for variety
)

plt.title("Energy Sources 2050", fontsize=16, fontweight='bold', pad=20, color='darkgreen')  # Changed color

plt.setp(autotexts, size=12, weight='normal', color='slategray')  # Adjust style
plt.setp(texts, size=10, weight='light')

# Changed legend location and removed title
ax.legend(
    wedges, energy_sources,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.05),  # Modifying legend placement
    ncol=3,
    fontsize=12
)

# Adding grid for enhanced visualization
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()