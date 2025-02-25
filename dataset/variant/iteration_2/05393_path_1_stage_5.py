import matplotlib.pyplot as plt

genres = ['Fantasy', 'Non-fiction', 'Historical', 'Science Fiction', 'Mystery', 'Fiction']
genre_distribution = [25, 20, 15, 15, 10, 15]

age_groups = ['30-39', '10-19', '0-9', '50-59', '60+', '40-49', '20-29']
books_read = [8, 5, 2, 11, 13, 9, 7]
variability = [0.5, 1, 1.5, 1.2, 1.3, 1.6, 2]

single_color = '#4CAF50'

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Bar Chart
ax1.barh(age_groups, books_read, color=single_color, height=0.6, xerr=variability, capsize=5)
ax1.set_xlabel('Books Consumed Per Year', fontsize=12)

for idx, value in enumerate(books_read):
    ax1.text(value + 0.3, idx, f'{value} reads', va='center', ha='left', fontsize=10, color='darkblue')

ax1.tick_params(axis='y', labelsize=12)

# Pie Chart
ax2.pie(genre_distribution, labels=genres, autopct='%1.1f%%', startangle=90,
        colors=[single_color] * len(genres))
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)
ax2.axis('equal') 

plt.tight_layout()
plt.subplots_adjust(wspace=0.4)
plt.show()