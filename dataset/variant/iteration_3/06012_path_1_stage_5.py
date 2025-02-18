import numpy as np
import matplotlib.pyplot as plt

brightness = np.array([5.1, 5.4, 5.7, 6.0, 6.3, 6.5, 7.0, 7.5, 8.0, 4.2, 4.5, 4.8, 3.1, 3.3,
                       3.9, 2.7, 2.5, 1.0, -1.5, 0.8, -1.0, -2.4, -2.3])
temperature = np.array([3000, 3200, 3500, 3700, 4000, 4300, 5000, 5200, 6000, 7000, 8000,
                        9000, 12000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 
                        50000, 55000, 60000])
new_brightness = np.array([6.8, 7.8, 2.3, 1.6, 0.5, -1.2, 0.0, -3.0])
new_temperature = np.array([3600, 4800, 33000, 37000, 22000, 31000, 26000, 38000])

combined_brightness = np.concatenate((brightness, new_brightness))
combined_temperature = np.concatenate((temperature, new_temperature))

sorted_indices = np.argsort(combined_brightness)
sorted_brightness = combined_brightness[sorted_indices]
sorted_temperature = combined_temperature[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#D5AAFF', '#85E3FF', '#FFDDC1', '#FFC3A0', '#B9FBC0', '#FFABAB', '#A0E7E5', '#FF9CEE']
ax.bar(range(len(sorted_brightness)), sorted_brightness, color=colors * ((len(sorted_brightness) // len(colors)) + 1), edgecolor='green', linestyle='--', hatch='/')

ax.set_title('Luminous Twinkles - Revamped Vision', fontsize=18, fontweight='light')
ax.set_xlabel('Celestial Index', fontsize=11, style='italic')
ax.set_ylabel('Light Intensity (Stellar Magnitude)', fontsize=11, style='italic')
ax.invert_yaxis()

ax.legend(['Intensity Value'], loc='upper right', fontsize=10, title='Key', title_fontsize='11')
ax.grid(True, which='major', linestyle='-.', linewidth='0.75', color='gray')

plt.tight_layout()
plt.show()