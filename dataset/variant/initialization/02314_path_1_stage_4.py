import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020])

sci_fi = np.array([10, 11, 13, 12, 15, 14])
mystery = np.array([8, 9, 10, 9, 11, 10])
fantasy = np.array([12, 13, 14, 13, 15, 16])
historical_fiction = np.array([7, 8, 9, 8, 10, 9])
dystopian = np.array([9, 10, 11, 10, 12, 11])

errors = {
    "Sci-Fi": np.array([1, 0.8, 1.2, 0.9, 1.1, 0.7]),
    "Mystery": np.array([0.5, 0.4, 0.6, 0.5, 0.7, 0.3]),
    "Fantasy": np.array([1, 0.9, 1.3, 1.1, 1.5, 1.2]),
    "Historical Fiction": np.array([0.4, 0.3, 0.5, 0.4, 0.6, 0.2]),
    "Dystopian": np.array([0.6, 0.5, 0.7, 0.6, 0.8, 0.4]),
}

new_colors = ['#1f77b4', '#ffbb78', '#c5b0d5', '#ff9896', '#9467bd']

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(years - 0.3, sci_fi, xerr=errors["Sci-Fi"], label='Sci-Fi', color=new_colors[0], height=0.2, alpha=0.75, edgecolor='gray', hatch='/')
ax.barh(years, mystery, xerr=errors["Mystery"], label='Mystery', color=new_colors[1], height=0.2, alpha=0.75, edgecolor='gray', hatch='\\')
ax.barh(years + 0.3, fantasy, xerr=errors["Fantasy"], label='Fantasy', color=new_colors[2], height=0.2, alpha=0.75, edgecolor='gray', hatch='-')
ax.barh(years + 0.6, historical_fiction, xerr=errors["Historical Fiction"], label='Historical Fiction', color=new_colors[3], height=0.2, alpha=0.75, edgecolor='gray', hatch='|')
ax.barh(years + 0.9, dystopian, xerr=errors["Dystopian"], label='Dystopian', color=new_colors[4], height=0.2, alpha=0.75, edgecolor='gray', hatch='*')

ax.set_title("Literature Trends Over Years", fontsize=18, fontweight='bold', pad=15, color='darkred')
ax.set_xlabel("Books per Person", fontsize=12, color='darkblue')
ax.set_ylabel("Year", fontsize=12, color='darkblue')
ax.set_yticks(years)
ax.legend(title='Book Genres', fontsize=10, loc='upper left', frameon=True, borderpad=1, shadow=True)
ax.grid(True, linestyle='-.', linewidth=0.5, alpha=0.5)

fig.patch.set_facecolor('lightgray')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()