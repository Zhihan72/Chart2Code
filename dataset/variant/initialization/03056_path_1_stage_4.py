import matplotlib.pyplot as plt
import squarify

innovations = {
    'Artificial Intelligence': [120, 180, 90, 60],
    'Nanotechnology': [300, 250],
    'Interstellar Propulsion': [400]
}

innovation_labels = [
    'AI - Terrapolis\n(120 GU)', 'AI - Omicron\n(180 GU)', 'AI - Hyperia\n(90 GU)', 'AI - Xylon\n(60 GU)',
    'Nano - Solara\n(300 GU)', 'Nano - Vortex\n(250 GU)',
    'Propulsion - Helios\n(400 GU)'
]
sizes = [value for sublist in innovations.values() for value in sublist]
labels = [f'{lbl}' for lbl in innovation_labels]

colors = ['#FF6347', '#FF4500', '#FF8C00', '#FFA500',
          '#7B68EE', '#6A5ACD',
          '#8A2BE2']

fig, ax = plt.subplots(figsize=(14, 9))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.75, ax=ax, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="white", linewidth=2.5)

plt.title("Intergalactic Innovation Fair 3023\nBreakthroughs and Their Market Influence", fontsize=16, fontweight='regular', style='italic')

ax.set_facecolor('#f5f5dc')

ax.annotate('Most Significant\nFunding Shift\nin Propulsion Tech\n(400 GU)', xy=(0.35, 0.05), xycoords='axes fraction', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#8A2BE2", alpha=0.5))

ax.grid(visible=True, linestyle='--', linewidth=0.7, alpha=0.3)

fig.legend(labels=["AI Advancements", "Nano Breakthroughs", "Propulsion Tech"], 
           loc="upper right", fontsize=10, title="Fields of Innovation",
           edgecolor="black", shadow=True)

plt.tight_layout(rect=[0, 0, 0.9, 1])
plt.show()