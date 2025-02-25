import matplotlib.pyplot as plt
import numpy as np

years = np.array([2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040])
smart_features = np.array([14, 16, 18, 20, 22, 25, 27, 30, 33, 36, 39, 43, 48])

milestones = {
    2030: 'Context',
    2035: 'Sentiment',
    2040: 'Emotion'
}

fig, ax1 = plt.subplots(figsize=(14, 6))
fig.tight_layout(pad=5.0)

ax1.plot(years, smart_features, marker='o', linestyle='-', color='darkgreen', linewidth=2, label='Smart Features')
ax1.set_title('Tech Evolution: AI Assistants', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Smart Features', fontsize=12, color='darkgreen')
ax1.tick_params(axis='y', labelcolor='darkgreen')

for year, milestone in milestones.items():
    idx = np.where(years == year)[0][0]
    ax1.annotate(milestone,
                 xy=(year, smart_features[idx]),
                 xytext=(10, 10),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'),
                 fontsize=10,
                 color='olive')
    ax1.scatter(year, smart_features[idx], color='gold', zorder=5)

ax1.axvspan(2030, 2035, alpha=0.1, color='brown', label='Context/Emotion')

ax1.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()