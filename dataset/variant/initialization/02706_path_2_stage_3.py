import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
import matplotlib.cm as cm

# Original dataset
gravitational_anomalies = np.array([1.2, 1.8, 2.3, 1.7, 2.5, 3.1, 2.8, 3.5, 2.9, 3.8, 4.2, 4.5, 3.0, 4.1])
organic_signature_strengths = np.array([2.1, 2.5, 2.8, 3.2, 2.9, 3.0, 3.3, 3.7, 3.1, 3.5, 3.6, 3.9, 3.2, 3.8])
sensor_sizes = np.array([100, 120, 150, 110, 130, 170, 140, 160, 135, 180, 190, 200, 145, 185])
colors = np.array(['#20B2AA', '#FF1493', '#7FFF00', '#DC143C', '#00CED1',
                   '#9400D3', '#F4A460', '#5F9EA0', '#FF6347', '#4682B4',
                   '#32CD32', '#FFD700', '#FF4500', '#8A2BE2'])

# Additional data series
additional_grav_anomalies = np.array([2.0, 3.6, 4.0, 4.3, 4.4])
additional_org_sig_strengths = np.array([2.4, 3.4, 3.5, 3.6, 4.0])
additional_sensor_sizes = np.array([125, 175, 180, 200, 175])
additional_colors = np.array(['#FFA07A', '#9370DB', '#EEE8AA', '#98FB98', '#AFEEEE'])

# Combine original and additional data
gravitational_anomalies = np.concatenate((gravitational_anomalies, additional_grav_anomalies))
organic_signature_strengths = np.concatenate((organic_signature_strengths, additional_org_sig_strengths))
sensor_sizes = np.concatenate((sensor_sizes, additional_sensor_sizes))
colors = np.concatenate((colors, additional_colors))

norm = Normalize(vmin=min(gravitational_anomalies), vmax=max(gravitational_anomalies))
cmap = cm.viridis

plt.figure(figsize=(14, 8))
plt.scatter(gravitational_anomalies, organic_signature_strengths, s=sensor_sizes, c=colors, 
            alpha=0.85, edgecolors=cmap(norm(gravitational_anomalies)), linewidth=2, zorder=2)

plt.gca().set_facecolor('#f0f8ff')

plt.title("Cosmic Exploration by Humanoid Drones:\nIntergalactic Scatter in the\nAndromeda Mission 2077", fontsize=18, fontweight='bold', y=1.02)
plt.xlabel("Gravitational Anomaly (arbitrary units)", fontsize=14, labelpad=10)
plt.ylabel("Organic Signature Strength (arbitrary units)", fontsize=14, labelpad=10)

plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

for i in range(len(gravitational_anomalies)):
    plt.annotate(f'P{i+1}', 
                 (gravitational_anomalies[i], organic_signature_strengths[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9,
                 arrowprops=dict(arrowstyle='->', lw=0.5, color='gray'))

plt.xticks(np.arange(1, 5.5, 0.5))
plt.yticks(np.arange(2, 4.5, 0.5))

plt.tight_layout()
plt.show()