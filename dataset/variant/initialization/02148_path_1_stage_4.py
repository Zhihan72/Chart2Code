import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
bike_rentals = np.array([12, 15, 18, 22, 25, 30, 35, 33, 28, 24, 20, 18])
scooter_rentals = np.array([7, 9, 11, 15, 18, 28, 34, 31, 24, 19, 17, 13])

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(months, bike_rentals, marker='o', linestyle='-', color='darkgreen', linewidth=2)
ax.plot(months, scooter_rentals, marker='s', linestyle='--', color='darkblue', linewidth=2)

annotations_bikes = {
    'Mar': ('Special Spring', 18),
    'Jun': ('Festive Ride', 30),
    'Sep': ('School Rush', 28),
}

for month, (text, value) in annotations_bikes.items():
    ax.annotate(
        text,
        xy=(month, value),
        xytext=(0, 10),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='darkgreen'),
        fontsize=10,
        color='darkgreen'
    )

ax.set_title('Greenford Transportation Analysis\nCycle Rentals in 2022', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Rental Month', fontsize=12)
ax.set_ylabel('Number of Rentals (thousands)', fontsize=12)

ax.set_ylim(0, 40)
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45, fontsize=10)

plt.tight_layout()
plt.show()