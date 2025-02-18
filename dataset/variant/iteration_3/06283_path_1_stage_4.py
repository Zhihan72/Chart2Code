import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Manually altered bird counts but maintaining structure (11 elements each)
sparrows = np.array([180, 350, 480, 615, 675, 920, 965, 1050, 1280, 1350, 1450])
hawks = np.array([120, 220, 310, 365, 415, 470, 510, 590, 680, 720, 780])
swallows = np.array([310, 370, 420, 480, 510, 655, 705, 820, 870, 1050, 1130])
pelicans = np.array([55, 65, 68, 85, 95, 125, 135, 170, 190, 195, 245])
geese = np.array([95, 160, 210, 340, 480, 620, 720, 810, 880, 980, 1150])

bird_migrations = np.vstack([sparrows, hawks, swallows, pelicans, geese])

fig, ax = plt.subplots(figsize=(14, 8))

single_color = '#66b3ff'

ax.stackplot(years, bird_migrations, colors=[single_color]*bird_migrations.shape[0], alpha=0.8)

ax.set_title("Birds Flying Patterns Over the Years (2010-2020)\nObserving Different Species", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Timeline", fontsize=12)
ax.set_ylabel("Count of Birds", fontsize=12)

ax.annotate('Sparrow Rise Insight', xy=(2013, 615), xytext=(2010, 1600),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Pinnacle of Hawk Wanderers', xy=(2019, 720), xytext=(2017, 1400),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.xticks(rotation=45)

plt.tight_layout(rect=[0, 0, 1, 1])

plt.show()