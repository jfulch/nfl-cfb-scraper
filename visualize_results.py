import csv
import matplotlib.pyplot as plt

# Read data from the CSV file
university_data = {}
with open('data/university_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        university = row['University']
        data = row['Data'].split(', ')
        university_data[university] = data

# Extract the lengths of each item in the dictionary
university_lengths = {k: len(v) for k, v in university_data.items()}

# Sort the dictionary by the number of entries and select the top 10
sorted_universities = dict(sorted(university_lengths.items(), key=lambda item: item[1], reverse=True)[:10])

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