import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020])

sci_fi = np.array([10, 11, 13, 12, 15, 14])
mystery = np.array([8, 9, 10, 9, 11, 10])
fantasy = np.array([12, 13, 14, 13, 15, 16])
historical_fiction = np.array([7, 8, 9, 8, 10, 9])

errors = {
    "Sci-Fi": np.array([1, 0.8, 1.2, 0.9, 1.1, 0.7]),
    "Mystery": np.array([0.5, 0.4, 0.6, 0.5, 0.7, 0.3]),
    "Fantasy": np.array([1, 0.9, 1.3, 1.1, 1.5, 1.2]),
    "Historical Fiction": np.array([0.4, 0.3, 0.5, 0.4, 0.6, 0.2]),
}

# New set of colors for each genre
new_colors = ['#e377c2', '#17becf', '#bcbd22', '#7f7f7f']

fig, ax = plt.subplots(figsize=(12, 7))

ax.barh(years - 0.3, sci_fi, xerr=errors["Sci-Fi"], label='Sci-Fi', color=new_colors[0], height=0.2, alpha=0.8)
ax.barh(years - 0.1, mystery, xerr=errors["Mystery"], label='Mystery', color=new_colors[1], height=0.2, alpha=0.8)
ax.barh(years + 0.1, fantasy, xerr=errors["Fantasy"], label='Fantasy', color=new_colors[2], height=0.2, alpha=0.8)
ax.barh(years + 0.3, historical_fiction, xerr=errors["Historical Fiction"], label='Historical Fiction', color=new_colors[3], height=0.2, alpha=0.8)

ax.set_title("Literary Trends in Litville:\n2015-2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Average Number of Books Read per Person", fontsize=14)
ax.set_ylabel("Year", fontsize=14)
ax.set_yticks(years)
ax.legend(title='Genres', fontsize=12, loc='lower right')
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()