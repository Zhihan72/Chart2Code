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
virtual_reality_usage = logistic_growth(years, x0=2022, L=40)
ai_assistants_usage = logistic_growth(years, x0=2021, L=45)

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, email_usage, social_media_usage, video_conferencing_usage, messaging_apps_usage, 
             mobile_apps_usage, iot_devices_usage, virtual_reality_usage, ai_assistants_usage,
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f'], alpha=0.8)

ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 600)
ax.set_xticks(np.arange(1980, 2025, 5))
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()