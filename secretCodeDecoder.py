import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    # Fetching info from URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data_div = soup.find('div', class_=['c6', 'doc-content'])

    if not data_div:
        print("No information found")
        return

    # Find all table elements with each data point.
    elements = data_div.find_all('td')

    # Process the td elements to remove text and into an array
    processed_data = []
    for i in range(0, len(elements), 3):
        x = elements[i].get_text().strip()
        char = elements[i+1].get_text().strip()
        y = elements[i+2].get_text().strip()
        # setting a forumla for the elements to be added into new array without text
        processed_data.append(f"{x}{char}{y}")

    # Putting data into object for easier usage later
    char_positions = {}
    max_x, max_y = 0, 0
    for item in processed_data:
        if len(item) <= 5:
            char_pos = -1
        for special_char in ['░', '█', '▀']:
            char_pos = item.find(special_char)
            if char_pos != -1:
                break
        
        if char_pos != -1:
                item.strip()
                x = int(item[:char_pos])
                char = item[char_pos]
                y = int(item[char_pos+1:])
                char_positions[(x, y)] = char
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    # Creation of the grid to use for indexing
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    for (x, y), char in char_positions.items():
        grid[max_y - y][x] = char

    print("\nDecoded message:")
    for row in grid:
        print(''.join(row))

# Using new function
url1 = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url2 = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"

decode_secret_message(url1)
decode_secret_message(url2)