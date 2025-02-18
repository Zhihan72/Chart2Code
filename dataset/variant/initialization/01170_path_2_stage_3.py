import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

novels_published = 150 * (1.1 ** np.arange(len(years)))
poetry_published = 100 + 20 * np.log1p(np.arange(len(years)))
short_stories_published = 200 + 30 * np.sqrt(np.arange(len(years)))
essays_published = 50 * np.exp(0.1 * np.arange(len(years)))

fig, axs = plt.subplots(1, 2, figsize=(14, 5))

axs[0].plot(years, novels_published, color='#1f77b4', marker='o', linewidth=2, linestyle='-')
axs[0].plot(years, poetry_published, color='#ff7f0e', marker='^', linewidth=2, linestyle='--')
axs[0].plot(years, short_stories_published, color='#2ca02c', marker='s', linewidth=2, linestyle='-.')
axs[0].plot(years, essays_published, color='#d62728', marker='x', linewidth=2, linestyle=':')

axs[0].set_title('A Decade of Diverse Literary Works (2020-2030)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Number of Works Published', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(np.arange(0, 801, 100))
axs[0].annotate('Poetry Boom', xy=(2025, poetry_published[5]), xytext=(2026, 150),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

growth_novels = np.diff(novels_published) / novels_published[:-1] * 100
growth_poetry = np.diff(poetry_published) / poetry_published[:-1] * 100
growth_short_stories = np.diff(short_stories_published) / short_stories_published[:-1] * 100
growth_essays = np.diff(essays_published) / essays_published[:-1] * 100

growth_years = years[1:]

axs[1].plot(growth_years, growth_novels, color='#1f77b4', linestyle='-')
axs[1].plot(growth_years, growth_poetry, color='#ff7f0e', linestyle='--')
axs[1].plot(growth_years, growth_short_stories, color='#2ca02c', linestyle='-.')
axs[1].plot(growth_years, growth_essays, color='#d62728', linestyle=':')

axs[1].set_title('Year-over-Year Growth Percentage by Genre', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Growth Percentage (%)', fontsize=12)
axs[1].set_xticks(growth_years)
axs[1].set_xticklabels(growth_years, rotation=45)
axs[1].set_yticks(np.arange(-20, 81, 20))

plt.tight_layout()
plt.show()