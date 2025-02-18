import matplotlib.pyplot as plt
import squarify

contributions = [450, 200, 300, 100, 150]
total_contribution = sum(contributions)
sizes = [c / total_contribution * 100 for c in contributions]
colors = ['#FFD700', '#87CEFA', '#7FFFD4', '#FF4500', '#8B4513']

fig, ax = plt.subplots(figsize=(14, 8))
squarify.plot(sizes=sizes, color=colors, alpha=0.7, edgecolor="black", linewidth=1.5)

plt.axis('off')
plt.tight_layout()
plt.show()