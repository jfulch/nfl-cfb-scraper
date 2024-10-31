import csv
import matplotlib.pyplot as plt

# Read data from the CSV file
university_data = {}
with open('data/university_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        university = row['University']
        player = row['Player']
        if university in university_data:
            university_data[university].append(player)
        else:
            university_data[university] = [player]

def get_school_stats(school):
    # Get the list of players for the school
    players = university_data.get(school, [])
    print(f'The current number of NFL players from {school} are: {len(players)}')
    
    # Print the dictionary entries for passed in school
    print(f'The Players of {school} are:')
    for player in players:
        print('-' + player)

#print(university_data.get('USC'))
get_school_stats('USC')
get_school_stats('UCLA')
get_school_stats('Air Force')
get_school_stats('Kansas State')

# Aggregate the number of players for each university
university_counts = {university: len(players) for university, players in university_data.items()}

# Sort the universities by the number of players
sorted_universities = dict(sorted(university_counts.items(), key=lambda item: item[1], reverse=True)[:15])

# Create a bar chart for the top 10 schools
plt.figure(figsize=(15, 5))
bars = plt.bar(sorted_universities.keys(), sorted_universities.values())
plt.xlabel('University')
plt.ylabel('# of NFL Players')
plt.title('Top Universities by Number of Current NFL Players')
plt.xticks(rotation=90)
plt.tight_layout()

# Annotate each bar with the number of players
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

plt.show()

# # Create a pie chart for the top 10 schools
# plt.figure(figsize=(8, 8))
# plt.pie(sorted_universities.values(), labels=sorted_universities.keys(), autopct='%1.1f%%')
# plt.title('Distribution of Entries for Top 10 Universities')
# plt.show()