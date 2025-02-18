import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1980, 2025, 0.25)

def logistic_growth(t, L=100, k=0.1, x0=2000):
    return L / (1 + np.exp(-k * (t - x0)))

email_usage = logistic_growth(years, x0=2000, L=80)
social_media_usage = logistic_growth(years, x0=2010, L=90)
video_conferencing_usage = logistic_growth(years, x0=2015, L=85)
messaging_apps_usage = logistic_growth(years, x0=2010, L=100)
mobile_apps_usage = logistic_growth(years, x0=2008, L=95)
iot_devices_usage = logistic_growth(years, x0=2020, L=50)

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, email_usage, social_media_usage, video_conferencing_usage, messaging_apps_usage, 
             mobile_apps_usage, iot_devices_usage,
             colors=['#FFD700', '#87CEEB', '#FF69B4', '#32CD32', '#FF4500', '#8A2BE2'], alpha=0.8)

ax.set_title("Evolution of Digital Communication Technologies\n(1980 - 2024)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Global Usage (% Normalized)', fontsize=14)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 500)
ax.set_xticks(np.arange(1980, 2025, 5))
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()