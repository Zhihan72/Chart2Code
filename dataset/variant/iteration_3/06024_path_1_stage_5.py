import matplotlib.pyplot as plt

modes_of_transport = ['Cycling', 'Automobiles', 'Buses & Trains', 'On Foot', 'Two-wheelers']
weekday_usage = [25, 10, 20, 40, 5]
weekend_usage = [20, 20, 25, 30, 5]

single_color = '#66b3ff'
explode = (0.1, 0, 0, 0, 0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 14))

# Donut pie chart for weekday usage
wedges1, texts1, autotexts1 = ax1.pie(
    weekday_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=[single_color] * len(modes_of_transport),
    explode=explode,
    shadow=True,
    wedgeprops=dict(width=0.3)
)
plt.setp(texts1, size=10, weight='bold')
plt.setp(autotexts1, size=9, weight='bold', color='white')
ax1.set_title("Transport, Weekday", fontsize=14, fontweight='bold', pad=20)
ax1.axis('equal')
ax1.legend(wedges1, modes_of_transport, title="Transport Modes", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

# Donut pie chart for weekend usage
wedges2, texts2, autotexts2 = ax2.pie(
    weekend_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=[single_color] * len(modes_of_transport),
    explode=explode,
    shadow=True,
    wedgeprops=dict(width=0.3)
)
plt.setp(texts2, size=10, weight='bold')
plt.setp(autotexts2, size=9, weight='bold', color='white')
ax2.set_title("Transport, Weekend", fontsize=14, fontweight='bold', pad=20)
ax2.axis('equal')
ax2.legend(wedges2, modes_of_transport, title="Transport Modes", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

fig.suptitle("Travel Patterns of Residents", fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()