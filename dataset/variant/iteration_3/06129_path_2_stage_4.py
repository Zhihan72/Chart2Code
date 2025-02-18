import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

heating = np.array([310, 340, 280, 200, 140, 130, 140, 220, 270, 180, 310, 350])  # Altered values
cooling = np.array([60, 80, 100, 290, 300, 370, 400, 200, 380, 170, 50, 60])    # Altered values
lighting = np.array([80, 100, 80, 120, 90, 110, 110, 100, 90, 90, 100, 100])   # Altered values
appliances = np.array([112, 130, 108, 122, 120, 125, 130, 115, 110, 105, 115, 120])  # Altered values

# Calculate based on the new altered values
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