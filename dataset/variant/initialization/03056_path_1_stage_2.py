import matplotlib.pyplot as plt
import squarify

# Market share data in "galactic units"
innovations = {
    'Artificial Intelligence': [120, 180, 90, 60],
    'Quantum Computing': [150, 200, 160],
    'Nanotechnology': [300, 250],
    'Interstellar Propulsion': [400]
}

# Flattened labels and sizes
innovation_labels = [
    'AI - Earth\n(120 GU)', 'AI - Zephyria\n(180 GU)', 'AI - Kronos\n(90 GU)', 'AI - Zogtron\n(60 GU)',
    'QC - Earth\n(150 GU)', 'QC - Zephyria\n(200 GU)', 'QC - Kronos\n(160 GU)',
    'Nano - Earth\n(300 GU)', 'Nano - Zephyria\n(250 GU)',
    'Propulsion - Earth\n(400 GU)'
]
sizes = [value for sublist in innovations.values() for value in sublist]
labels = [f'{lbl}' for lbl in innovation_labels]

colors = ['#FF6347', '#FF4500', '#FF8C00', '#FFA500',
          '#7FFF00', '#32CD32', '#228B22',
          '#7B68EE', '#6A5ACD',
          '#8A2BE2']

# Plot setup
fig, ax = plt.subplots(figsize=(14, 9))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.75, ax=ax, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="white", linewidth=2.5)

plt.title("Galactic Tech Expo 3023\nInnovations and Their Market Share", fontsize=16, fontweight='regular', style='italic')

ax.set_facecolor('#f5f5dc')  # Using a different face color for the axes
ax.annotate('AI Dominates\nwith 4 sectors', xy=(0.7, 0.7), xycoords='axes fraction', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#FF6347", alpha=0.5))

ax.annotate('Largest Single\nInvestment in\nPropulsion\n(400 GU)', xy=(0.35, 0.05), xycoords='axes fraction', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#8A2BE2", alpha=0.5))

# Additional stylistic deviations
ax.grid(visible=True, linestyle='--', linewidth=0.7, alpha=0.3)  # Adding a dashed grid

# Re-positioned legend with border
fig.legend(labels=["AI", "Quantum Computing", "Nanotechnology", "Interstellar Propulsion"], 
           loc="upper right", fontsize=10, title="Innovation Categories",
           edgecolor="black", shadow=True)

plt.tight_layout(rect=[0, 0, 0.9, 1])  # Adjust the layout for the re-positioned legend
plt.show()