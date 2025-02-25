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

investment_proportion = np.array([5, 7, 8, 10, 11, 14, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 34, 36, 39, 42, 45])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)
fig.tight_layout(pad=5.0)

ax1.plot(years, smart_features, marker='o', linestyle='-', color='royalblue', linewidth=2, label='Smart Features')
ax1.set_title('Tech Evolution: AI Assistants', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Smart Features', fontsize=12, color='royalblue')
ax1.tick_params(axis='y', labelcolor='royalblue')

for year, milestone in milestones.items():
    idx = np.where(years == year)[0][0]
    ax1.annotate(milestone,
                 xy=(year, smart_features[idx]),
                 xytext=(10, 10),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'),
                 fontsize=10,
                 color='darkred')
    ax1.scatter(year, smart_features[idx], color='red', zorder=5)

ax1.axvspan(2022, 2027, alpha=0.1, color='purple', label='Voice/NLP')
ax1.axvspan(2030, 2035, alpha=0.1, color='orange', label='Context/Emotion')

ax1.legend(loc='upper left', fontsize=10)

ax2.plot(years, investment_proportion, marker='s', linestyle='--', color='seagreen', linewidth=2, label='AI Investment (%)')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Investment Prop (%)', fontsize=12, color='seagreen')
ax2.tick_params(axis='y', labelcolor='seagreen')

ax2.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()