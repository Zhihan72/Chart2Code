import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

heating = np.array([350, 310, 280, 220, 180, 140, 130, 140, 200, 270, 310, 340])
cooling = np.array([50, 60, 100, 200, 300, 370, 400, 380, 290, 170, 80, 60])
lighting = np.array([100, 90, 80, 90, 100, 110, 120, 110, 100, 90, 80, 100])
appliances = np.array([120, 110, 105, 115, 120, 125, 130, 128, 122, 115, 108, 112])

overall_consumption = heating + cooling + lighting + appliances
monthly_savings = 0.1 * overall_consumption

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, heating, marker='x', linestyle='-.', color='darkorange', linewidth=1.5, label='Heat Use')
ax.plot(months, cooling, marker='p', linestyle='-', color='darkgreen', linewidth=2, label='Cool Effort')
ax.plot(months, lighting, marker='h', linestyle='--', color='purple', linewidth=1, label='Light Spending')
ax.plot(months, appliances, marker='D', linestyle=':', color='cyan', linewidth=1.5, label='Device Usage')
ax.plot(months, monthly_savings, marker='d', linestyle='-', color='magenta', linewidth=2, label='Eco Savings')

annotations = [
    ('Jan', heating[0], 'Yearly start,\nHigh heat use'),
    ('Jul', cooling[6], 'Top cool requirement'),
    ('Dec', lighting[11], 'More light needed')
]

for (month, value, text) in annotations:
    ax.annotate(text, xy=(month, value), xytext=(5, -30), textcoords='offset points',
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightblue', alpha=0.5))

ax.set_title('Energy Trends and Savings Overview', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Time of Year', fontsize=12)
ax.set_ylabel('Power Use (kWh)', fontsize=12)

ax.legend(title='Usage Categories', loc='upper right', fontsize=9)

ax.grid(True, linestyle='-', alpha=0.3)
ax.spines['top'].set_linestyle('--')
ax.spines['right'].set_linestyle('--')
ax.spines['top'].set_color('lightgray')
ax.spines['right'].set_color('lightgray')

plt.tight_layout()
plt.show()