import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

novels_published = 150 * (1.1 ** np.arange(len(years)))
poetry_published = 100 + 20 * np.log1p(np.arange(len(years)))
short_stories_published = 200 + 30 * np.sqrt(np.arange(len(years)))
essays_published = 50 * np.exp(0.1 * np.arange(len(years)))

fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Changed colors for the first subplot
axs[0].plot(years, novels_published, color='#e41a1c', marker='o', linewidth=2, linestyle='-')
axs[0].plot(years, poetry_published, color='#377eb8', marker='^', linewidth=2, linestyle='--')
axs[0].plot(years, short_stories_published, color='#4daf4a', marker='s', linewidth=2, linestyle='-.')
axs[0].plot(years, essays_published, color='#984ea3', marker='x', linewidth=2, linestyle=':')

axs[0].set_title('Literary Genres Over the Years (2020-2030)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Publication Year', fontsize=12)
axs[0].set_ylabel('Works Released', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(np.arange(0, 801, 100))
axs[0].annotate('Rise of Poetry', xy=(2025, poetry_published[5]), xytext=(2026, 150),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

growth_novels = np.diff(novels_published) / novels_published[:-1] * 100
growth_poetry = np.diff(poetry_published) / poetry_published[:-1] * 100
growth_short_stories = np.diff(short_stories_published) / short_stories_published[:-1] * 100
growth_essays = np.diff(essays_published) / essays_published[:-1] * 100

growth_years = years[1:]

# Changed colors for the second subplot
axs[1].plot(growth_years, growth_novels, color='#e41a1c', linestyle='-')
axs[1].plot(growth_years, growth_poetry, color='#377eb8', linestyle='--')
axs[1].plot(growth_years, growth_short_stories, color='#4daf4a', linestyle='-.')
axs[1].plot(growth_years, growth_essays, color='#984ea3', linestyle=':')

axs[1].set_title('Annual Growth Rate by Category', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year of Study', fontsize=12)
axs[1].set_ylabel('Growth Rate (%)', fontsize=12)
axs[1].set_xticks(growth_years)
axs[1].set_xticklabels(growth_years, rotation=45)
axs[1].set_yticks(np.arange(-20, 81, 20))

plt.tight_layout()
plt.show()