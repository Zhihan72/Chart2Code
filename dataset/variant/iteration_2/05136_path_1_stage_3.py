import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

years = np.arange(2010, 2020)

red_giant_magnitudes = np.array([3.5, 3.4, 3.3, 3.3, 3.2, 3.1, 3.1, 3.0, 2.9, 2.8])
white_dwarf_magnitudes = np.array([12.5, 12.4, 12.3, 12.2, 12.1, 12.0, 11.9, 11.8, 11.7, 11.6])
main_sequence_magnitudes = np.array([4.0, 3.9, 3.9, 3.8, 3.8, 3.7, 3.7, 3.6, 3.5, 3.5])
blue_supergiant_magnitudes = np.array([1.5, 1.4, 1.5, 1.6, 1.6, 1.5, 1.4, 1.4, 1.3, 1.2])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, red_giant_magnitudes, color='orange', marker='o', linestyle='-', linewidth=2)
ax.plot(years, white_dwarf_magnitudes, color='purple', marker='s', linestyle='--', linewidth=2)
ax.plot(years, main_sequence_magnitudes, color='teal', marker='^', linestyle='-.', linewidth=2)
ax.plot(years, blue_supergiant_magnitudes, color='blue', marker='d', linestyle=':', linewidth=2)

ax.fill_between(years, red_giant_magnitudes, color='orange', alpha=0.1)
ax.fill_between(years, white_dwarf_magnitudes, color='purple', alpha=0.1)
ax.fill_between(years, main_sequence_magnitudes, color='teal', alpha=0.1)
ax.fill_between(years, blue_supergiant_magnitudes, color='blue', alpha=0.1)

def smooth_trendline(x, y):
    spline = make_interp_spline(x, y, k=3)
    x_range = np.linspace(min(x), max(x), 300)
    smooth_y = spline(x_range)
    return x_range, smooth_y

rg_x, rg_smooth = smooth_trendline(years, red_giant_magnitudes)
wd_x, wd_smooth = smooth_trendline(years, white_dwarf_magnitudes)
ms_x, ms_smooth = smooth_trendline(years, main_sequence_magnitudes)
bs_x, bs_smooth = smooth_trendline(years, blue_supergiant_magnitudes)

ax.plot(rg_x, rg_smooth, color='orange', linestyle='-', alpha=0.3)
ax.plot(wd_x, wd_smooth, color='purple', linestyle='--', alpha=0.3)
ax.plot(ms_x, ms_smooth, color='teal', linestyle='-.', alpha=0.3)
ax.plot(bs_x, bs_smooth, color='blue', linestyle=':', alpha=0.3)

ax.set_title('Decade-long Brightness Monitoring of Different Stars', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Apparent Magnitude\n(Lower is Brighter)', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.show()