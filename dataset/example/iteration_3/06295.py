import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Title: Technological Evolution of Personal Assistants: A 20-Year Journey
# Description: We will examine the growth and major milestones in the development of personal AI assistants from 2020 to 2040. The line chart will display the number of smart features introduced each year. Subplots will provide additional context with the introduction of significant breakthroughs during that period.

# Data: Number of Smart Features Introduced Annually
years = np.arange(2020, 2041)
smart_features = np.array([2, 4, 5, 6, 7, 9, 10, 12, 14, 16, 18, 20, 22, 25, 27, 30, 33, 36, 39, 43, 48])

# Significant breakthroughs and milestones:
milestones = {
    2022: 'Voice Command Recognition',
    2027: 'Natural Language Processing',
    2030: 'Contextual Understanding',
    2035: 'Sentiment Analysis',
    2040: 'Emotion Simulation'
}

# Auxiliary data: The proportion of AI development invested into personal assistants (in percentage)
investment_proportion = np.array([5, 7, 8, 10, 11, 14, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 34, 36, 39, 42, 45])

# Plot setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)
fig.tight_layout(pad=5.0)

# Plot smart features introduced over years (Primary line chart)
ax1.plot(years, smart_features, marker='o', linestyle='-', color='royalblue', linewidth=2, label='Smart Features Introduced')
ax1.set_title('Technological Evolution of Personal Assistants: A 20-Year Journey', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Number of Smart Features', fontsize=12, color='royalblue')
ax1.tick_params(axis='y', labelcolor='royalblue')

# Adding labels for milestones
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

# Highlight areas of significant breakthroughs
ax1.axvspan(2022, 2027, alpha=0.1, color='purple', label='Voice & NLP Era')
ax1.axvspan(2030, 2035, alpha=0.1, color='orange', label='Contextual & Emotional Era')

# Legend
ax1.legend(loc='upper left', fontsize=10)

# Plot investment proportions (Secondary line chart)
ax2.plot(years, investment_proportion, marker='s', linestyle='--', color='seagreen', linewidth=2, label='Investment Proportion in AI Development')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Investment Proportion (%)', fontsize=12, color='seagreen')
ax2.tick_params(axis='y', labelcolor='seagreen')

# Legend
ax2.legend(loc='upper left', fontsize=10)

# Layout adjustment and show plot
plt.tight_layout()
plt.show()