import matplotlib.pyplot as plt

activities = [
    "Holo", 
    "Debris Hunt", 
    "Virtual Tour", 
    "Zero-G", 
    "Nebula Paint", 
    "Stargaze", 
    "Comet Chase", 
    "Teleport Darts"
]
popularity_percentages = [22, 18, 12, 15, 9, 10, 8, 6]
new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', 
              '#f58231', '#911eb4', '#46f0f0', '#f032e6']

fig, ax1 = plt.subplots(figsize=(10, 7))

ax1.pie(popularity_percentages, labels=activities, autopct='%1.1f%%', startangle=140, colors=new_colors,
        explode=[0.1, 0, 0, 0, 0, 0, 0, 0], wedgeprops=dict(edgecolor='black'))

ax1.set_title("Galactic Rec Preferences", fontsize=16, fontweight='bold', pad=20)

plt.show()