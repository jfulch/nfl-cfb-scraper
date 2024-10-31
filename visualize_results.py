import matplotlib.pyplot as plt

# Create a bar chart for the top 10 schools
plt.figure(figsize=(10, 5))
plt.bar(sorted_universities.keys(), sorted_universities.values())
plt.xlabel('University')
plt.ylabel('Number of Entries')
plt.title('Top 10 Universities by Number of Entries')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Create a pie chart for the top 10 schools
plt.figure(figsize=(8, 8))
plt.pie(sorted_universities.values(), labels=sorted_universities.keys(), autopct='%1.1f%%')
plt.title('Distribution of Entries for Top 10 Universities')
plt.show()