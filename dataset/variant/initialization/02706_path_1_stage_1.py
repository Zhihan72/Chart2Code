import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
import matplotlib.cm as cm

# Original data points for the Andromeda Mission
gravitational_anomalies = np.array([2.3, 3.1, 1.8, 2.9, 1.2, 4.5, 3.8, 3.5, 2.5, 3.0, 1.7, 4.1, 2.8, 4.2])
organic_signature_strengths = np.array([3.0, 2.5, 3.9, 2.8, 3.1, 3.7, 2.1, 3.5, 2.9, 3.2, 3.3, 3.6, 3.8, 3.0])
sensor_sizes = np.array([150, 200, 120, 160, 100, 190, 180, 110, 140, 130, 135, 170, 145, 185])
colors = np.array(['#4682B4', '#8A2BE2', '#FFD700', '#F4A460', '#FF6347', 
                   '#FF4500', '#9400D3', '#32CD32', '#FF1493', '#DC143C', 
                   '#7FFF00', '#5F9EA0', '#20B2AA', '#00CED1'])

norm = Normalize(vmin=gravitational_anomalies.min(), vmax=gravitational_anomalies.max())
cmap = cm.viridis

plt.figure(figsize=(14, 8))
plt.scatter(gravitational_anomalies, organic_signature_strengths, s=sensor_sizes, c=colors, 
            alpha=0.85, edgecolors=cmap(norm(gravitational_anomalies)), linewidth=2, zorder=2)
plt.gca().set_facecolor('#f0f8ff')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

plt.title("Cosmic Exploration by Humanoid Drones:\nIntergalactic Scatter in the\nAndromeda Mission 2077", fontsize=18, fontweight='bold', y=1.02)
plt.xlabel("Gravitational Anomaly (arbitrary units)", fontsize=14, labelpad=10)
plt.ylabel("Organic Signature Strength (arbitrary units)", fontsize=14, labelpad=10)

plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

for i in range(len(gravitational_anomalies)):
    plt.annotate(f'P{i+1}', 
                 (gravitational_anomalies[i], organic_signature_strengths[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9,
                 arrowprops=dict(arrowstyle='->', lw=0.5, color='gray'))

plt.xticks(np.arange(1, 5.5, 0.5))
plt.yticks(np.arange(2, 4.5, 0.5))

legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=f'Probe {i+1}',
                              markerfacecolor=colors[i], markersize=10, alpha=0.85) for i in range(len(colors))]
plt.legend(handles=legend_elements, title="Probes", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

plt.tight_layout()
plt.show()