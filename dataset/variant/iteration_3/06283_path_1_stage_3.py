import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

sparrows = np.array([200, 300, 400, 550, 700, 850, 950, 1100, 1250, 1400, 1500])
hawks = np.array([100, 200, 300, 350, 400, 450, 500, 550, 600, 700, 750])
swallows = np.array([300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1100])
pelicans = np.array([50, 60, 70, 80, 100, 120, 140, 160, 180, 200, 250])
geese = np.array([100, 150, 200, 350, 500, 600, 700, 800, 900, 1000, 1100])

bird_migrations = np.vstack([sparrows, hawks, swallows, pelicans, geese])

fig, ax = plt.subplots(figsize=(14, 8))

single_color = '#66b3ff'

ax.stackplot(years, bird_migrations, colors=[single_color]*bird_migrations.shape[0], alpha=0.8)

# Randomly altered textual elements
ax.set_title("Birds Flying Patterns Over the Years (2010-2020)\nObserving Different Species", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Timeline", fontsize=12)
ax.set_ylabel("Count of Birds", fontsize=12)

ax.annotate('Sparrow Rise Insight', xy=(2013, 700), xytext=(2010, 1600),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Pinnacle of Hawk Wanderers', xy=(2019, 700), xytext=(2017, 1400),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.xticks(rotation=45)

plt.tight_layout(rect=[0, 0, 1, 1])

plt.show()