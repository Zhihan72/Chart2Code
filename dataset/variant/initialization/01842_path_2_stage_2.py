import matplotlib.pyplot as plt
import numpy as np

device_categories = [
    'Smart Lighting',
    'Smart Thermostats',
    'Smart Speakers',
    'Smart TVs',
    'Smart Appliances',
    'Smart Security Systems',
    'Smart Assistants',
    'Smart Plugs'
]

energy_consumption_percentages = [12, 20, 8, 25, 15, 10, 5, 5]

# Define a single color for all bars
single_color = 'skyblue'

fig, ax = plt.subplots(figsize=(16, 10))
bars = ax.barh(device_categories, energy_consumption_percentages, color=single_color, edgecolor='black', height=0.6)

ax.set_xlabel('Energy Consumption (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('Smart Devices', fontsize=12, fontweight='bold')
ax.set_title('Tech Energy Consumption:\nPercentage Contribution of Devices in Smart Homes (2023)', fontsize=16, fontweight='bold', loc='left', pad=20)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{width}%', va='center', ha='left', fontsize=11, fontweight='bold', color='darkred')

ax.set_xlim(0, 100)
ax.xaxis.grid(True, linestyle='--', alpha=0.7, color='gray')
ax.invert_yaxis()

annotations = [
    '💡 Smart Lighting: Enhances ambiance, saves energy',
    '🌡️ Smart Thermostats: Automates climate control, improves efficiency',
    '🔊 Smart Speakers: Provides connectivity, minimal power use',
    '📺 Smart TVs: Entertainment, significant energy draw',
    '🔌 Smart Appliances: Streamline chores, considerable power',
    '🔒 Smart Security Systems: Ensure safety, moderate power',
    '🗣️ Smart Assistants: Enhance productivity, minimal energy',
    '🔌 Smart Plugs: Monitor power usage, improve control'
]

plt.legend(bars, annotations, title="Device Significance", loc='upper right',
                    bbox_to_anchor=(1.35, 1), fontsize=10, title_fontsize='11', frameon=False)

plt.tight_layout()
plt.show()