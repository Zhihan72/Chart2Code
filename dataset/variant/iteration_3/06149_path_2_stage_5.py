import matplotlib.pyplot as plt

# Data
basketball_sleep_hours = [7.5, 8, 8.1, 7.9, 8.3, 8, 7.8, 8.2, 8.3, 8.1, 7.9, 8, 7.5, 8, 8.2, 8.4, 8.6, 7.8, 8.1, 7.9]

fig, ax = plt.subplots(figsize=(8, 6))

ax.boxplot(basketball_sleep_hours, patch_artist=True,
           boxprops=dict(color='navy'),
           whiskerprops=dict(color='navy'),
           capprops=dict(color='navy'),
           flierprops=dict(marker='o', color='navy', markersize=6, alpha=0.6),
           medianprops=dict(color='darkorange', linewidth=2))

plt.tight_layout()
plt.show()