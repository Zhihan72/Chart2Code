import matplotlib.pyplot as plt
import numpy as np

# Define time period: months over 10 years
months = np.arange(1, 121)  

# Create sales data with seasonal variation
sales_compact = 100 + 10 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 600, 120)
sales_sedan = 120 + 20 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 700, 120)
sales_suv = 150 + 15 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 800, 120)
sales_truck = 130 + 5 * np.sin(np.linspace(0, 24 * np.pi, 120)) + np.linspace(0, 500, 120)

milestones = {
    12: "Year 1\nMilestone",
    36: "Year 3\nMilestone",
    60: "Year 5\nMilestone",
    84: "Year 7\nMilestone",
    120: "Year 10\nMilestone"
}

events = {
    24: "Model Launch",
    48: "Regulation Change",
    96: "Eco Subsidy"
}

plt.figure(figsize=(14, 8))
plt.plot(months, sales_compact, color='blue', linestyle='-', linewidth=2, marker='o', markersize=4)
plt.plot(months, sales_sedan, color='green', linestyle='--', linewidth=2, marker='s', markersize=4)
plt.plot(months, sales_suv, color='red', linestyle='-.', linewidth=2, marker='^', markersize=4)
plt.plot(months, sales_truck, color='purple', linestyle=':', linewidth=2, marker='d', markersize=4)

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

plt.title("The Rise of Electric Vehicles:\nComprehensive Monthly Sales Analysis Over 10 Years", fontsize=16, weight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Number of EVs Sold", fontsize=12)
plt.xticks(np.arange(0, 121, step=12), 
           ['M0', 'M12', 'M24', 'M36', 'M48', 'M60', 'M72', 'M84', 'M96', 'M108', 'M120'], fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()

plt.show()