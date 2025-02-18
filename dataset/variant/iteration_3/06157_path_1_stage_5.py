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

# Changed marker and line style
ax1.plot(years, smart_features, marker='s', linestyle='--', color='royalblue', linewidth=2, label='Smart Features')
ax1.set_title('Tech Evolution: AI Assistants with Dynamics', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Smart Features', fontsize=12, color='royalblue')
ax1.tick_params(axis='y', labelcolor='royalblue')

for year, milestone in milestones.items():
    idx = np.where(years == year)[0][0]
    ax1.annotate(milestone,
                 xy=(year, smart_features[idx]),
                 xytext=(-30, -30),  # changed annotation offset
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.3', color='teal'),  # changed arrow properties
                 fontsize=10,
                 color='teal')
    ax1.scatter(year, smart_features[idx], color='crimson', zorder=5)  # changed milestone scatter color

# Changed vspan style
ax1.axvspan(2030, 2035, alpha=0.15, color='gray', label='Context/Emotion')

# Changed legend location and fontsize
ax1.legend(loc='lower right', fontsize=9)

# Added grid lines
ax1.grid(True, which='both', linestyle=':', linewidth=0.5)

# Added border
for spine in ax1.spines.values():
    spine.set_edgecolor('navy')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.show()