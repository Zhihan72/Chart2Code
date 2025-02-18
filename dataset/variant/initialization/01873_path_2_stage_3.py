import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)

ice_cream_sales = np.array([
    14, 22.8, 11.2, 16.8, 19, 21, 13, 10.5, 20, 22.3,
    18.5, 24.5, 23.5, 25.5, 12.3, 25, 15.5, 11, 17.3, 14.2,
    24, 20.5, 11.8, 13.5, 15, 22, 21.5, 10, 19.7, 12.3,
    16
])

plt.figure(figsize=(14, 7))
plt.plot(years, ice_cream_sales, color='orange', marker='o', linestyle='-', linewidth=2, markersize=6)

highlight_indices = [0, 10, 20, 30]
for i in highlight_indices:
    plt.annotate(
        '',
        (years[i], ice_cream_sales[i]),
        textcoords="offset points",
        xytext=(-5, 10),
        ha='center',
        fontsize=10,
        color='blue'
    )

plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(10, 26, 2))

plt.tight_layout()
plt.show()