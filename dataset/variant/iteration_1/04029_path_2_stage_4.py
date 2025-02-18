import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

energy = [400, 385, 370, 350, 330, 310, 290, 270, 250, 230, 215]
transport = [300, 295, 285, 275, 260, 245, 230, 215, 200, 185, 170]
industry = [250, 245, 240, 230, 220, 210, 200, 190, 180, 170, 160]
total_emissions = np.array(energy) + np.array(transport) + np.array(industry)

fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

ax1.stackplot(years, energy, transport, industry,
              colors=['#e6194b', '#3cb44b', '#ffe119'], alpha=0.7)

ax2.plot(years, total_emissions, 'k--', linewidth=2)

ax1.tick_params(axis='x', labelrotation=45)

plt.tight_layout()
plt.show()