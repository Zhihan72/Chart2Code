import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

novels_published = 150 * (1.1 ** np.arange(len(years)))
poetry_published = 100 + 20 * np.log1p(np.arange(len(years)))
short_stories_published = 200 + 30 * np.sqrt(np.arange(len(years)))
essays_published = 50 * np.exp(0.1 * np.arange(len(years)))
plays_published = 60 + 40 * np.sin(np.linspace(0, 2 * np.pi, len(years)))

# Shuffle the colors for the data series
color_list = ['#d62728', '#1f77b4', '#9467bd', '#2ca02c', '#ff7f0e']

fig, axs = plt.subplots(2, 1, figsize=(14, 10))

axs[0].plot(years, novels_published, label='Rainfall', color=color_list[0], marker='o', linewidth=2, linestyle='-')
axs[0].plot(years, poetry_published, label='Sunshine', color=color_list[1], marker='^', linewidth=2, linestyle='--')
axs[0].plot(years, short_stories_published, label='Clouds', color=color_list[2], marker='s', linewidth=2, linestyle='-.')
axs[0].plot(years, essays_published, label='Wind', color=color_list[3], marker='x', linewidth=2, linestyle=':')
axs[0].plot(years, plays_published, label='Thunder', color=color_list[4], marker='d', linewidth=2, linestyle='-')

axs[0].set_title('Weather Patterns Over the Years', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Time', fontsize=12)
axs[0].set_ylabel('Frequency', fontsize=12)

axs[0].legend(loc='upper left', title='Weather Type', fontsize=10, frameon=False)
axs[0].grid(True, linestyle='--', alpha=0.6)

axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(np.arange(0, 801, 100))

axs[0].axvline(x=2030, color='gray', linestyle='--', linewidth=0.8, label='Notable Year')

axs[0].annotate('Sunshine Peak', xy=(2025, poetry_published[5]), xytext=(2026, 150),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

growth_novels = np.diff(novels_published) / novels_published[:-1] * 100
growth_poetry = np.diff(poetry_published) / poetry_published[:-1] * 100
growth_short_stories = np.diff(short_stories_published) / short_stories_published[:-1] * 100
growth_essays = np.diff(essays_published) / essays_published[:-1] * 100
growth_plays = np.diff(plays_published) / plays_published[:-1] * 100

growth_years = years[1:]

axs[1].plot(growth_years, growth_novels, label='Rainfall Growth %', color=color_list[0], linestyle='-')
axs[1].plot(growth_years, growth_poetry, label='Sunshine Growth %', color=color_list[1], linestyle='--')
axs[1].plot(growth_years, growth_short_stories, label='Clouds Growth %', color=color_list[2], linestyle='-.')
axs[1].plot(growth_years, growth_essays, label='Wind Growth %', color=color_list[3], linestyle=':')
axs[1].plot(growth_years, growth_plays, label='Thunder Growth %', color=color_list[4], linestyle='-')

axs[1].set_title('Annual Growth in Weather Conditions', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Time Frame', fontsize=12)
axs[1].set_ylabel('Growth %', fontsize=12)

axs[1].legend(loc='upper left', title='Condition Type', fontsize=10, frameon=False)
axs[1].grid(True, linestyle='--', alpha=0.6)

axs[1].set_xticks(growth_years)
axs[1].set_xticklabels(growth_years, rotation=45)
axs[1].set_yticks(np.arange(-20, 81, 20))

plt.tight_layout()
plt.show()