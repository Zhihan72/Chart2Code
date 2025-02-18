import matplotlib.pyplot as plt
import squarify

# Market share data in "galactic units"
innovations = {
    'Artificial Intelligence': [120, 180, 90, 60],
    'Quantum Computing': [150, 200, 160],
    'Nanotechnology': [300, 250],
    'Interstellar Propulsion': [400]
}

# Labels for each subcategory
innovation_labels = [
    'AI - Earth\n(120 GU)', 'AI - Zephyria\n(180 GU)', 'AI - Kronos\n(90 GU)', 'AI - Zogtron\n(60 GU)',
    'QC - Earth\n(150 GU)', 'QC - Zephyria\n(200 GU)', 'QC - Kronos\n(160 GU)',
    'Nano - Earth\n(300 GU)', 'Nano - Zephyria\n(250 GU)',
    'Propulsion - Earth\n(400 GU)'
]

# Flatten data and labels for plotting
sizes = [value for sublist in innovations.values() for value in sublist]
labels = [f'{lbl}' for lbl in innovation_labels]

# New color set for categories
colors = ['#FF6347', '#FF4500', '#FF8C00', '#FFA500',  # AI
          '#7FFF00', '#32CD32', '#228B22',            # QC
          '#7B68EE', '#6A5ACD',                       # Nano
          '#8A2BE2']                                  # Propulsion

# Plot setup
fig, ax = plt.subplots(figsize=(14, 9))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7, ax=ax, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="black", linewidth=1.5)

plt.title("Galactic Tech Expo 3023\nInnovations and Their Market Share", fontsize=16, fontweight='bold')
ax.axis('off')
ax.set_facecolor('#f0f8ff')

# Annotation updates with new color
ax.annotate('AI Dominates\nwith 4 sectors', xy=(0.7, 0.7), xycoords='axes fraction', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#FF6347", alpha=0.6))

ax.annotate('Largest Single\nInvestment in\nPropulsion\n(400 GU)', xy=(0.35, 0.05), xycoords='axes fraction', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#8A2BE2", alpha=0.6))

# Legend
fig.legend(labels=["AI", "Quantum Computing", "Nanotechnology", "Interstellar Propulsion"], 
           loc="upper left", fontsize=10, title="Innovation Categories")

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()