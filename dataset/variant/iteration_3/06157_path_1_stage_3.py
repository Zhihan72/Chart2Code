import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2041)
smart_features = np.array([2, 4, 5, 6, 7, 9, 10, 12, 14, 16, 18, 20, 22, 25, 27, 30, 33, 36, 39, 43, 48])

milestones = {
    2022: 'Voice Cmd',
    2027: 'NLP',
    2030: 'Context',
    2035: 'Sentiment',
    2040: 'Emotion'
}

fig, ax1 = plt.subplots(figsize=(14, 6))
fig.tight_layout(pad=5.0)

# Changed the color for the main line plot and associated elements
ax1.plot(years, smart_features, marker='o', linestyle='-', color='darkgreen', linewidth=2, label='Smart Features')
ax1.set_title('Tech Evolution: AI Assistants', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Smart Features', fontsize=12, color='darkgreen')
ax1.tick_params(axis='y', labelcolor='darkgreen')

# Changed annotation color and scatter plot color
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

# Changed the color of shaded spans
ax1.axvspan(2022, 2027, alpha=0.1, color='teal', label='Voice/NLP')
ax1.axvspan(2030, 2035, alpha=0.1, color='brown', label='Context/Emotion')

ax1.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()