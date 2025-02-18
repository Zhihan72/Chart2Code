import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020])

sci_fi = np.array([14, 10, 12, 11, 13, 15])
mystery = np.array([10, 11, 8, 9, 10, 9])
fantasy = np.array([15, 12, 14, 16, 13, 13])
historical_fiction = np.array([9, 8, 10, 7, 9, 8])

errors = {
    "Sci-Fi": np.array([1, 0.8, 1.2, 0.9, 1.1, 0.7]),
    "Mystery": np.array([0.5, 0.4, 0.6, 0.5, 0.7, 0.3]),
    "Fantasy": np.array([1, 0.9, 1.3, 1.1, 1.5, 1.2]),
    "Historical Fiction": np.array([0.4, 0.3, 0.5, 0.4, 0.6, 0.2]),
}

single_color = '#1f77b4'  # Using a single color for all data series

fig, ax = plt.subplots(figsize=(12, 7))

# Create horizontal bar chart
ax.barh(years - 0.3, sci_fi, color=single_color, xerr=errors["Sci-Fi"], label="Sci-Fi", height=0.2, capsize=5, alpha=0.8)
ax.barh(years - 0.1, mystery, color=single_color, xerr=errors["Mystery"], label="Mystery", height=0.2, capsize=5, alpha=0.8)
ax.barh(years + 0.1, fantasy, color=single_color, xerr=errors["Fantasy"], label="Fantasy", height=0.2, capsize=5, alpha=0.8)
ax.barh(years + 0.3, historical_fiction, color=single_color, xerr=errors["Historical Fiction"], label="Historical Fiction", height=0.2, capsize=5, alpha=0.8)

ax.set_title("Lit Trends:\n2015-20", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Avg Books/Person", fontsize=14)  # Switched x-label to Avg Books/Person because the bars are horizontal
ax.set_ylabel("Yr", fontsize=14)
ax.set_yticks(years)
ax.set_yticklabels(years)
ax.legend()
plt.tight_layout()
plt.show()