import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
base_url = 'https://www.espn.com/nfl/college/_/letter/'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Initialize an empty list to store the data
university_data = []

for letter in alphabet:
    response = requests.get(base_url + letter, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    # Find the table containing the list of presidents
    table = soup.find('table', {'class': 'tablehead'})

    # Check if the table exists
    if table:
        university_name = None
        # Iterate over the rows in the table
        for row in table.find_all('tr'):
            # Check if the row has the class 'stathead' to get the university name
            if 'stathead' in row.get('class', []):
                university_name = row.get_text(strip=True)
            elif university_name:
                # Collect the data into a dictionary
                row_data = [td.get_text(strip=True) for td in row.find_all('td')]
                if row_data:
                    university_data.append({
                        'University': university_name,
                        'Data': ', '.join(row_data)  # Flatten the list into a single string
                    })
    else:
        print("Table not found")

# Write the data to a CSV file
with open('data/university_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['University', 'Data']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for data in university_data:
        writer.writerow(data)

print("Data has been successfully written to data/university_data.csv")
    

def get_school_stats(school):
    # Get the list of players for the school
    players = university_data.get(school, [])
    print(f'The current number of NFL players from {school} are: {len(players)}')
    
    # Print the dictionary entries for 'USC'
    print(f'The Players of {school} are:')
    for player in players:
        print('\t' + '\t'.join(player))

#get_school_stats('USC')
#get_school_stats('UCLA')
#get_school_stats('Air Force')
#get_school_stats('Kansas State')