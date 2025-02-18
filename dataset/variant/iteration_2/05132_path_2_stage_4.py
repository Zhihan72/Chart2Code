import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Fad', 'Bef', 'Car', 'Rap', 'Tay', 'Zun', 
    'Jal', 'Aug', 'Sep', 'Oct', 'Nov', 'Dex'
])

san_francisco_temps = np.array([17, 12, 14, 11, 16, 13, 18, 18, 15, 17, 12, 11])
new_york_temps = np.array([7, 2, 18, 0, 10, 24, 27, 26, 22, 13, 16, 4])
tokyo_temps = np.array([22, 5, 6, 10, 9, 15, 19, 27, 24, 19, 14, 6])
paris_temps = np.array([9, 6, 5, 12, 22, 19, 21, 6, 18, 14, 16, 9])
sydney_temps = np.array([20, 23, 22, 22, 16, 19, 14, 13, 16, 23, 18, 14])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, san_francisco_temps, label='SF Bay', color='purple', marker='s', linestyle='--')
ax.plot(months, new_york_temps, label='NYC', color='orange', marker='x', linestyle='-.')
ax.plot(months, tokyo_temps, label='TKY', color='teal', marker='d', linestyle=':')
ax.plot(months, paris_temps, label='PRS', color='grey', marker='*', linestyle='-')
ax.plot(months, sydney_temps, label='SYD', color='pink', marker='+', linestyle='--')

ax.set_title('Monthly Temp for Cities', fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel('Calendar', fontsize=14)
ax.set_ylabel('Celsius', fontsize=14)

ax.legend(title='Urban Areas', fontsize=12, title_fontsize=14, loc='lower left')
ax.grid(False)

# Keeping the same annotations as originally specified, no random change applied here.
for (month, temp_san_francisco) in zip(months, san_francisco_temps):
    if temp_san_francisco in [11, 18]:
        ax.annotate(f'{temp_san_francisco}°C', xy=(month, temp_san_francisco), xytext=(-20, -25), 
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', lw=1))

ax.spines['top'].set_linewidth(0.5)
ax.spines['right'].set_linewidth(0.5)

plt.tight_layout()
plt.show()