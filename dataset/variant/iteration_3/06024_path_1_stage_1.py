import matplotlib.pyplot as plt
import numpy as np

modes_of_transport = ['Cycling', 'Automobiles', 'Buses & Trains', 'On Foot', 'Two-wheelers']
weekday_usage = [20, 40, 25, 10, 5]
weekend_usage = [25, 30, 20, 20, 5]

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
explode = (0.1, 0, 0, 0, 0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

wedges1, texts1, autotexts1 = ax1.pie(
    weekday_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True
)
plt.setp(texts1, size=10, weight='bold')
plt.setp(autotexts1, size=9, weight='bold', color='white')
ax1.set_title("Transport, Weekday", fontsize=14, fontweight='bold', pad=20)
ax1.axis('equal')
ax1.legend(wedges1, modes_of_transport, title="Transport Modes", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

wedges2, texts2, autotexts2 = ax2.pie(
    weekend_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True
)
plt.setp(texts2, size=10, weight='bold')
plt.setp(autotexts2, size=9, weight='bold', color='white')
ax2.set_title("Transport, Weekend", fontsize=14, fontweight='bold', pad=20)
ax2.axis('equal')
ax2.legend(wedges2, modes_of_transport, title="Transport Modes", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

fig.suptitle("Travel Patterns of Residents", fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()