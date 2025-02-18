import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)

ice_cream_sales = np.array([
    10, 10.5, 11, 11.2, 11.8, 12.3, 13, 13.5, 14, 14.2, 
    15, 15.5, 16, 16.8, 17.3, 18, 18.5, 19, 19.7, 20, 
    20.5, 21, 21.5, 22, 22.3, 22.8, 23.5, 24, 24.5, 25, 
    25.5
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