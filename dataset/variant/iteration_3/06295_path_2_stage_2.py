import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2041)
smart_features = np.array([2, 4, 5, 6, 7, 9, 10, 12, 14, 16, 18, 20, 22, 25, 27, 30, 33, 36, 39, 43, 48])

milestones = {
    2022: 'Voice Command Recognition',
    2027: 'Natural Language Processing',
    2030: 'Contextual Understanding',
    2035: 'Sentiment Analysis',
    2040: 'Emotion Simulation'
}

investment_proportion = np.array([5, 7, 8, 10, 11, 14, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 34, 36, 39, 42, 45])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)
fig.tight_layout(pad=5.0)

# Changed color from 'royalblue' to 'darkorange'
ax1.plot(years, smart_features, marker='o', linestyle='-', color='darkorange', linewidth=2)
ax1.set_title('Technological Evolution of Personal Assistants: A 20-Year Journey', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Number of Smart Features', fontsize=12, color='darkorange')
ax1.tick_params(axis='y', labelcolor='darkorange')

for year, milestone in milestones.items():
    idx = np.where(years == year)[0][0]
    ax1.annotate(milestone,
                 xy=(year, smart_features[idx]),
                 xytext=(10, 10),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'),
                 fontsize=10,
                 # Changed color from 'darkred' to 'slateblue'
                 color='slateblue')
    # Changed color from 'red' to 'crimson'
    ax1.scatter(year, smart_features[idx], color='crimson', zorder=5)

# Changed color from 'purple' to 'lightgrey'
ax1.axvspan(2022, 2027, alpha=0.1, color='lightgrey')
# Changed color from 'orange' to 'lightcoral'
ax1.axvspan(2030, 2035, alpha=0.1, color='lightcoral')

# Changed color from 'seagreen' to 'teal'
ax2.plot(years, investment_proportion, marker='s', linestyle='--', color='teal', linewidth=2)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Investment Proportion (%)', fontsize=12, color='teal')
ax2.tick_params(axis='y', labelcolor='teal')

plt.tight_layout()
plt.show()