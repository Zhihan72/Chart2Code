import matplotlib.pyplot as plt
import numpy as np

sectors = ['Res', 'Comm', 'Ind', 'Edu', 'Rec']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

voltage_levels = np.array([
    [220, 215, 218, 220, 222, 224, 225, 230, 229, 228, 226, 225],
    [230, 228, 231, 233, 235, 238, 239, 240, 238, 237, 236, 234],
    [210, 215, 220, 225, 230, 235, 240, 245, 248, 250, 245, 240],
    [220, 222, 224, 226, 228, 230, 232, 234, 233, 231, 229, 227],
    [215, 218, 220, 222, 224, 226, 228, 230, 228, 226, 224, 222]
])

average_voltage = np.mean(voltage_levels, axis=0)

mask = np.tril(np.ones_like(voltage_levels, dtype=bool))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
fig.suptitle('City Power Monitoring\nVoltage Levels', fontsize=16, fontweight='bold')

heatmap = axes[0].imshow(np.ma.masked_array(voltage_levels, mask=~mask), cmap='cool', aspect='auto', interpolation='nearest')
cbar = fig.colorbar(heatmap, ax=axes[0])
cbar.set_label('Voltage (V)', fontsize=10)

axes[0].set_title('Voltage by Sector/Month', fontsize=12)
axes[0].set_xlabel('Mon', fontsize=10)
axes[0].set_ylabel('Sector', fontsize=10)
axes[0].set_xticks(np.arange(len(months)))
axes[0].set_xticklabels(months, fontsize=8, rotation=45)
axes[0].set_yticks(np.arange(len(sectors)))
axes[0].set_yticklabels(sectors, fontsize=8)

for i in range(len(sectors)):
    for j in range(len(months)):
        if i >= j:
            axes[0].text(j, i, f"{voltage_levels[i, j]}", ha='center', va='center', color='black', fontsize=7)

axes[1].plot(months, average_voltage, marker='o', color='blue', linewidth=2, label='Avg Voltage')
axes[1].set_title('Avg Voltage Trend', fontsize=12)
axes[1].set_xlabel('Mon', fontsize=10)
axes[1].set_ylabel('Avg Voltage (V)', fontsize=10)
axes[1].set_xticks(np.arange(len(months)))
axes[1].set_xticklabels(months, fontsize=8, rotation=45)
axes[1].grid(True, linestyle='--', alpha=0.7)
axes[1].legend(fontsize=9)
axes[1].set_ylim(200, 250)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()