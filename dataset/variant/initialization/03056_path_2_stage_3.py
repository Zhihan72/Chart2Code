import matplotlib.pyplot as plt
import squarify

# Market share data in "galactic units" without 'Quantum'
innovations = {
    'AI': [120, 180, 90, 60],
    'Nano': [300, 250],
    'Propulsion': [400]
}

# Labels for subcategories without 'Quantum'
innovation_labels = [
    'AI - Earth\n(120)', 'AI - Zephyria\n(180)', 'AI - Kronos\n(90)', 'AI - Zogtron\n(60)',
    'Nano - Earth\n(300)', 'Nano - Zephyria\n(250)',
    'Propulsion - Earth\n(400)'
]

# Flatten data and labels for plotting
sizes = [value for sublist in innovations.values() for value in sublist]
labels = [f'{lbl}' for lbl in innovation_labels]

# Shuffled colors for visualization, reduced to match new data size
colors = ['#32CD32', '#C71585', '#ADD8E6', '#FFB6C1', 
          '#FFD700', '#4169E1', 
          '#FF1493']

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 9))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7, ax=ax, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="black", linewidth=1.5)

# Set a concise title
plt.title("Galactic Tech 3023\nMarket Share", fontsize=16, fontweight='bold')

# Remove axis for clarity
ax.axis('off')

# Customizing plot background
ax.set_facecolor('#f0f8ff')

# Annotations for insights, adjusted the position for clarity.
ax.annotate('AI: 4 sectors', xy=(0.7, 0.8), xycoords='axes fraction', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#FFB6C1", alpha=0.6))

ax.annotate('Largest in Propulsion\n(400)', xy=(0.35, 0.05), xycoords='axes fraction', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#FFD700", alpha=0.6))

# Display a legend
fig.legend(labels=["AI", "Nano", "Propulsion"], 
           loc="upper left", fontsize=10, title="Tech")

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()