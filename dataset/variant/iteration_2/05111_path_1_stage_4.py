import matplotlib.pyplot as plt

activities = [
    "Gaming", 
    "Tourism", 
    "Sports", 
    "Painting", 
    "Stargazing"
]
popularity_percentages = [25, 15, 18, 10, 12]

colors = ['#ff9999', '#ffcc99', '#99ff99', '#c2c2f0', '#ffb3e6']

fig, ax1 = plt.subplots(figsize=(10, 7))

explode = [0.1, 0, 0, 0, 0]

ax1.pie(popularity_percentages, labels=activities, autopct='%1.1f%%', startangle=140, colors=colors,
        explode=explode, wedgeprops=dict(edgecolor='black'))

ax1.set_title("Galactic Preferences", fontsize=16, fontweight='bold', pad=20)

plt.show()