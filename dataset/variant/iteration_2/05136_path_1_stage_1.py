import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Updated years of observation
years = np.arange(2010, 2020)

# Updated artificial data for star magnitude
red_giant_magnitudes = np.array([3.5, 3.4, 3.3, 3.3, 3.2, 3.1, 3.1, 3.0, 2.9, 2.8])
white_dwarf_magnitudes = np.array([12.5, 12.4, 12.3, 12.2, 12.1, 12.0, 11.9, 11.8, 11.7, 11.6])
main_sequence_magnitudes = np.array([4.0, 3.9, 3.9, 3.8, 3.8, 3.7, 3.7, 3.6, 3.5, 3.5])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting with new color scheme
ax.plot(years, red_giant_magnitudes, label='Red Giant', color='orange', marker='o', linestyle='-', linewidth=2)
ax.plot(years, white_dwarf_magnitudes, label='White Dwarf', color='purple', marker='s', linestyle='--', linewidth=2)
ax.plot(years, main_sequence_magnitudes, label='Main Sequence', color='teal', marker='^', linestyle='-.', linewidth=2)

# Fill areas between the lines and the x-axis with new colors
ax.fill_between(years, red_giant_magnitudes, color='orange', alpha=0.1)
ax.fill_between(years, white_dwarf_magnitudes, color='purple', alpha=0.1)
ax.fill_between(years, main_sequence_magnitudes, color='teal', alpha=0.1)

# Spline interpolation for a smooth fitting line
def smooth_trendline(x, y):
    spline = make_interp_spline(x, y, k=3)
    x_range = np.linspace(min(x), max(x), 300)
    smooth_y = spline(x_range)
    return x_range, smooth_y

rg_x, rg_smooth = smooth_trendline(years, red_giant_magnitudes)
wd_x, wd_smooth = smooth_trendline(years, white_dwarf_magnitudes)
ms_x, ms_smooth = smooth_trendline(years, main_sequence_magnitudes)

ax.plot(rg_x, rg_smooth, color='orange', linestyle='-', alpha=0.3)
ax.plot(wd_x, wd_smooth, color='purple', linestyle='--', alpha=0.3)
ax.plot(ms_x, ms_smooth, color='teal', linestyle='-.', alpha=0.3)

# Set title and labels
ax.set_title('Decade-long Brightness Monitoring of Different Stars', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Apparent Magnitude\n(Lower is Brighter)', fontsize=14)

# Customize grid lines and tick marks
ax.grid(True, which='both', linestyle='--', alpha=0.6)
ax.minorticks_on()
ax.tick_params(axis='both', which='major', labelsize=12)

# Adding a legend
ax.legend(loc='upper right', fontsize=12, frameon=True)

# Annotate significant points and events
ax.annotate('Red Giant Brightness Increase', xy=(2011, 3.4), xytext=(2012, 3.6),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='darkorange')
ax.annotate('White Dwarf Slight Dimming', xy=(2013, 12.3), xytext=(2014, 12.5),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='indigo')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()