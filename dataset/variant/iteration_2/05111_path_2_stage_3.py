import matplotlib.pyplot as plt

activities = [
    "Holo", 
    "Debris Hunt", 
    "Virtual Tour", 
    "Zero-G", 
    "Nebula Paint", 
    "Stargaze"
]
popularity_percentages = [25, 20, 15, 18, 10, 12]
new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4']

fig, ax1 = plt.subplots(figsize=(10, 7))

ax1.pie(popularity_percentages, labels=activities, autopct='%1.1f%%', startangle=140, colors=new_colors,
        explode=[0.1, 0, 0, 0, 0, 0], wedgeprops=dict(edgecolor='black'))

ax1.set_title("Galactic Rec Preferences", fontsize=16, fontweight='bold', pad=20)

plt.show()