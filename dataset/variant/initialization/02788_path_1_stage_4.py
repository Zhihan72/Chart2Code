import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 121)

sales_compact = 100 + 10 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 600, 120)
sales_sedan = 120 + 20 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 700, 120)
sales_suv = 150 + 15 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 800, 120)

milestones = {
    12: "Milestone 1",
    36: "Special Event Y3",
    60: "Big Deal Y5",
    84: "Y7 Highlight",
    120: "Decade Mark"
}
events = {
    24: "Launch Model",
    48: "Policy Change",
    96: "Green Incentive"
}

plt.figure(figsize=(14, 8))
single_color_for_all = 'teal'
plt.plot(months, sales_compact, color=single_color_for_all, linestyle='--', linewidth=2.5, marker='D', markersize=5, label='Compact EV')
plt.plot(months, sales_sedan, color=single_color_for_all, linestyle=':', linewidth=2.5, marker='p', markersize=5, label='Sedan EV')
plt.plot(months, sales_suv, color=single_color_for_all, linestyle='-', linewidth=2.5, marker='h', markersize=5, label='Sport Utility EV')

for month, text in milestones.items():
    plt.annotate(text, (month, (sales_compact[month-1] + sales_sedan[month-1] + sales_suv[month-1]) / 3),
                 textcoords="offset points", xytext=(-15, 25), ha='center',
                 arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5))

for month, text in events.items():
    plt.annotate(text, (month, sales_sedan[month-1]), textcoords="offset points", xytext=(-20, -30), ha='center',
                 arrowprops=dict(facecolor='orange', arrowstyle='->', linewidth=1.5))

plt.title("Electric Vehicles Surge:\n10-Year Sales Overview", fontsize=16, weight='bold')
plt.xlabel("Month Number", fontsize=12)
plt.ylabel("EVs Sold Count", fontsize=12)
plt.xticks(np.arange(0, 121, step=12), 
           ['0m', '12m', '24m', '36m', '48m', '60m', '72m', '84m', '96m', '108m', '120m'], fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='upper right', fontsize=12)
plt.grid(False)
plt.tight_layout()
plt.show()