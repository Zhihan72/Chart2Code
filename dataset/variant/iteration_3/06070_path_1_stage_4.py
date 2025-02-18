import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
japan_speeds = [130, 200, 240, 270, 300, 320, 350]
france_speeds = [120, 160, 200, 270, 300, 320, 330]
germany_speeds = [100, 150, 200, 250, 280, 300, 320]
china_speeds = [0, 0, 0, 200, 250, 300, 350]
usa_speeds = [50, 100, 150, 200, 250, 280, 310]  # New data series for USA
italy_speeds = [70, 130, 180, 230, 260, 290, 330]  # New data series for Italy

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(decades, japan_speeds, marker='o', linestyle='-', linewidth=2, label='Japan', color='black')
ax.plot(decades, france_speeds, marker='s', linestyle='--', linewidth=2, label='France', color='darkgray')
ax.plot(decades, germany_speeds, marker='^', linestyle='-.', linewidth=2, label='Germany', color='lightgray')
ax.plot(decades, china_speeds, marker='d', linestyle=':', linewidth=2, label='China', color='gray')

# Adding plots for the new data series
ax.plot(decades, usa_speeds, marker='p', linestyle='-', linewidth=2, label='USA', color='darkblue')
ax.plot(decades, italy_speeds, marker='h', linestyle='--', linewidth=2, label='Italy', color='darkgreen')

ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 401, 50))

# Adding a legend to differentiate data series
ax.legend()

plt.tight_layout()
plt.show()