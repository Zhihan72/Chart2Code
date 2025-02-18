import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 121)

sales_compact = 100 + 10 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 600, 120)
sales_sedan = 120 + 20 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 700, 120)
sales_suv = 150 + 15 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 800, 120)
sales_truck = 130 + 5 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 500, 120)

sales_hatchback = 110 + 18 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 650, 120)
sales_ev = 140 + 12 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 550, 120)

milestones = {
    12: "Yr 1",
    36: "Yr 3",
    60: "Yr 5",
    84: "Yr 7",
    120: "Yr 10"
}

events = {
    24: "Launch",
    48: "Reg Change",
    96: "Eco Sub"
}

plt.figure(figsize=(14, 8))
plt.plot(months, sales_compact, color='blue', linestyle='-', linewidth=2, marker='o', markersize=4)
plt.plot(months, sales_sedan, color='blue', linestyle='--', linewidth=2, marker='s', markersize=4)
plt.plot(months, sales_suv, color='blue', linestyle='-.', linewidth=2, marker='^', markersize=4)
plt.plot(months, sales_truck, color='blue', linestyle=':', linewidth=2, marker='d', markersize=4)
plt.plot(months, sales_hatchback, color='blue', linestyle='-', linewidth=2, marker='*', markersize=4)
plt.plot(months, sales_ev, color='blue', linestyle='--', linewidth=2, marker='x', markersize=4)

for month, text in milestones.items():
    plt.annotate(text, 
                 (month, (sales_compact[month-1] + sales_sedan[month-1] + sales_suv[month-1] + sales_truck[month-1]) / 4),
                 textcoords="offset points", xytext=(-15, 25), ha='center',
                 arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5))

for month, text in events.items():
    plt.annotate(text, 
                 (month, sales_sedan[month-1]), 
                 textcoords="offset points", xytext=(-20, -30), ha='center',
                 arrowprops=dict(facecolor='orange', arrowstyle='->', linewidth=1.5))

plt.title("EV Sales: Monthly Over 10 Yrs", fontsize=16, weight='bold')
plt.xlabel("Mos", fontsize=12)
plt.ylabel("# EVs Sold", fontsize=12)
plt.xticks(np.arange(0, 121, step=12), ['M0', 'M12', 'M24', 'M36', 'M48', 'M60', 'M72', 'M84', 'M96', 'M108', 'M120'], fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()

plt.show()