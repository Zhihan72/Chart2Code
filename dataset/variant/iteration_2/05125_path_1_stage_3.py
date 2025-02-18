import matplotlib.pyplot as plt

franchises = ['Star Wars', 'Star Trek', 'Doctor Who', 'Dune', 'The Expanse', 'Others']
popularity_percentages = [30, 25, 15, 10, 10, 10]
colors = ['#ff4500', '#1e90ff', '#32cd32', '#ff8c00', '#6a5acd', '#ff1493']
explode = (0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(
    popularity_percentages, 
    explode=explode, 
    labels=franchises, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(edgecolor='white', linewidth=2, alpha=0.9)
)

ax.set_aspect('equal') 
plt.show()