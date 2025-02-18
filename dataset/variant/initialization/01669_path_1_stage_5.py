import matplotlib.pyplot as plt
import numpy as np

stages = ["Conceptualization", "R&D", "Pilot Testing", "Market Testing", "Full Deployment"]
percentages = [100, 80, 65, 50, 40]

fig, ax1 = plt.subplots(figsize=(8, 6))

# Horizontal Bar Chart for Funnel Representation
ax1.barh(stages, percentages, color=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00'], edgecolor='gray')
ax1.invert_yaxis()
ax1.set_xlim(0, 100)
ax1.set_xlabel("Percentage (%)", fontweight='bold')
ax1.set_title("Funnel Representation")

plt.tight_layout()
plt.show()