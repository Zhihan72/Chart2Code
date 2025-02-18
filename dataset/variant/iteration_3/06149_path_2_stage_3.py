import matplotlib.pyplot as plt

# Data
basketball_sleep_hours = [7.5, 8, 8.1, 7.9, 8.3, 8, 7.8, 8.2, 8.3, 8.1, 7.9, 8, 7.5, 8, 8.2, 8.4, 8.6, 7.8, 8.1, 7.9]
football_sleep_hours = [8.5, 8.1, 7.9, 8, 8.4, 8.2, 7.8, 8.1, 8.2, 8.3, 8.5, 8.4, 8.3, 8.1, 8.6, 8.7, 8.5, 8.3, 8.2, 8.4]
swimming_sleep_hours = [7.8, 7.5, 7.9, 8, 8.1, 8.3, 8.4, 7.9, 8, 7.7, 7.8, 8.2, 8, 7.9, 8.1, 8.5, 7.9, 8, 7.6, 8.1]
running_sleep_hours = [7.2, 7.5, 7.8, 7.7, 7.9, 7.6, 7.8, 7.6, 7.5, 7.7, 7.9, 8, 7.6, 7.8, 7.7, 8.1, 7.9, 7.5, 7.8, 7.6]
cycling_sleep_hours = [8.3, 8.1, 7.9, 8.4, 8.2, 8.6, 8.1, 8.3, 8.2, 8.7, 8.5, 8.3, 8.4, 8.2, 8.6, 8.1, 8.5, 8.3, 8.7, 8.2]

# Additional data for Yoga
yoga_sleep_hours = [8.2, 8.0, 8.1, 8.2, 8.4, 8.3, 8.1, 8.3, 8.4, 8.5, 8.3, 8.2, 8.4, 8.3, 8.1, 8.5, 8.2, 8.4, 8.3, 8.1]

sleep_hours_data = [basketball_sleep_hours, football_sleep_hours, swimming_sleep_hours, running_sleep_hours, cycling_sleep_hours, yoga_sleep_hours]

fig, ax = plt.subplots(figsize=(12, 8))

ax.boxplot(sleep_hours_data, patch_artist=True, notch=True,
           boxprops=dict(color='navy'),
           whiskerprops=dict(color='navy'),
           capprops=dict(color='navy'),
           flierprops=dict(marker='o', color='red', markersize=8, alpha=0.6),
           medianprops=dict(color='darkorange', linewidth=2))

plt.tight_layout()
plt.show()