import matplotlib.pyplot as plt
import numpy as np

days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
probe_A = np.array([250, 245, 243, 240, 242, 244, 248])
probe_B = np.array([252, 247, 245, 243, 244, 247, 251])
probe_C = np.array([249, 245, 244, 241, 243, 246, 250])

fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'royalblue'
ax1.plot(days, probe_A, '-o', color=color, markersize=6, linewidth=2, markerfacecolor=color)
ax1.plot(days, probe_B, '-s', color=color, markersize=6, linewidth=2, markerfacecolor=color)
ax1.plot(days, probe_C, '-^', color=color, markersize=6, linewidth=2, markerfacecolor=color)

ax1.set_xticks(np.arange(len(days)))
ax1.set_xticklabels(days)

plt.show()