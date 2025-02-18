import matplotlib.pyplot as plt

languages = ['Rust', 'Python', 'Java', 'JavaScript', 'C++', 'Go', 'Ruby', 'PHP']
usage_percentages = [4, 29, 16, 24, 12, 5, 7, 3]
colors = ['#98FB98', '#FF9999', '#99FF99', '#66B3FF', '#FFCC99', '#FFA07A', '#FFD700', '#C2C2F0']

fig, ax = plt.subplots(figsize=(9, 9))

ax.pie(
    usage_percentages, 
    labels=languages, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=(0.1, 0.1, 0, 0.1, 0, 0, 0.1, 0), 
    shadow=True, 
    wedgeprops=dict(width=0.3)
)

ax.axis('equal')
ax.set_title('Open Source Coding in 2025\nLanguage Popularity', fontsize=15, fontweight='bold', pad=20)
ax.legend(languages, title="Top Languages", loc='upper right', bbox_to_anchor=(1.2, 1))

plt.tight_layout()
plt.show()