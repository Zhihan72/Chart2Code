import matplotlib.pyplot as plt

modes_of_transport = ['Bicycles', 'Cars', 'Public Transport', 'Walking', 'Motorcycles']
weekday_usage = [20, 40, 25, 10, 5]
weekend_usage = [25, 30, 20, 20, 5]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.1, 0, 0, 0, 0)

# Modify the subplot arrangement to 2 rows x 1 column
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Plot the weekday donut chart
ax1.pie(
    weekday_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops=dict(width=0.3)
)
ax1.set_title("Weekday Transportation Preferences", fontsize=14, fontweight='bold')

# Plot the weekend donut chart
ax2.pie(
    weekend_usage,
    labels=modes_of_transport,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops=dict(width=0.3)
)
ax2.set_title("Weekend Transportation Preferences", fontsize=14, fontweight='bold')

fig.suptitle("Town Residents' Transportation Habits", fontsize=16, fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()