import matplotlib.pyplot as plt

energy_share = [20, 3, 33, 5, 25, 2, 12]
colors = ['#aec7e8', '#ff7f0e', '#2ca02c', '#1f77b4', '#8c564b', '#ffcc00', '#9467bd']

plt.figure(figsize=(10, 8))
plt.pie(
    energy_share, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3)  # Adding width creates the donut shape
)

plt.show()