import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2041)
smart_features = np.array([2, 4, 5, 6, 7, 9, 10, 12, 14, 16, 18, 20, 22, 25, 27, 30, 33, 36, 39, 43, 48])

milestones = {
    2022: 'Voice Recognition',
    2027: 'Language Processing',
    2030: 'Contextual Understanding',
    2035: 'Analysis of Sentiments',
    2040: 'Simulating Emotion'
}

investment_proportion = np.array([5, 7, 8, 10, 11, 14, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 34, 36, 39, 42, 45])
user_engagement = np.array([3, 4, 5, 6, 7, 9, 11, 13, 15, 18, 20, 23, 26, 30, 34, 39, 45, 52, 60, 69, 79])

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 18), sharex=True)
fig.tight_layout(pad=5.0)

ax1.plot(years, smart_features, marker='o', linestyle='-', color='darkorange', linewidth=2)
ax1.set_title('Evolution of Virtual Assistants Over 20 Years', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Smart Feature Count', fontsize=12, color='darkorange')
ax1.tick_params(axis='y', labelcolor='darkorange')

for year, milestone in milestones.items():
    idx = np.where(years == year)[0][0]
    ax1.annotate(milestone,
                 xy=(year, smart_features[idx]),
                 xytext=(10, 10),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'),
                 fontsize=10,
                 color='slateblue')
    ax1.scatter(year, smart_features[idx], color='crimson', zorder=5)

ax1.axvspan(2022, 2027, alpha=0.1, color='lightgrey')
ax1.axvspan(2030, 2035, alpha=0.1, color='lightcoral')

ax2.plot(years, investment_proportion, marker='s', linestyle='--', color='teal', linewidth=2)
ax2.set_ylabel('Investment Share (%)', fontsize=12, color='teal')
ax2.tick_params(axis='y', labelcolor='teal')

ax3.plot(years, user_engagement, marker='^', linestyle='-.', color='purple', linewidth=2)
ax3.set_xlabel('Timeline', fontsize=12)
ax3.set_ylabel('User Engagement Rate', fontsize=12, color='purple')
ax3.tick_params(axis='y', labelcolor='purple')

plt.tight_layout()
plt.show()