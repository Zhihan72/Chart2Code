import matplotlib.pyplot as plt

modes_of_transport = ['Cycling', 'Automobiles', 'Bus/Train', 'Foot', 'Scooters']
weekday_usage = [20, 40, 25, 10, 5]
weekend_usage = [25, 30, 20, 20, 5]

single_color = '#66b3ff'
explode = (0.1, 0, 0, 0, 0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

ax1.pie(
    weekday_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=[single_color] * len(modes_of_transport),
    explode=explode,
    wedgeprops=dict(width=0.3)
)
ax1.set_title("Transport on Weekdays", fontsize=14, fontweight='bold')

ax2.pie(
    weekend_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=[single_color] * len(modes_of_transport),
    explode=explode,
    wedgeprops=dict(width=0.3)
)
ax2.set_title("Leisure Transport", fontsize=14, fontweight='bold')

fig.suptitle("Locality Travel Patterns", fontsize=16, fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()