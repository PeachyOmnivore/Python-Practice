import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    # Fetch the content from the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with class 'c6' and 'doc-content'
    data_div = soup.find('div', class_=['c6', 'doc-content'])

    if not data_div:
        print("Could not find the data div in the document.")
        return

    # Find all td elements
    td_elements = data_div.find_all('td')

    # Process the td elements to add commas
    processed_data = []
    for i in range(0, len(td_elements), 3):
        x = td_elements[i].get_text().strip()
        char = td_elements[i+1].get_text().strip()
        y = td_elements[i+2].get_text().strip()
        processed_data.append(f"{x}{char}{y},")

    # Join the processed data
    char_data = ''.join(processed_data)
    # print(char_data)
    # Function to parse the character data
    def parse_char_data(data):
        return [tuple(item.split()) for item in data.split(',') if item.strip()]

    charArr = char_data.split(',')
    print(charArr)
    # Parse the data and store in a dictionary
    char_positions = {}
    max_x, max_y = 0, 0
    for item in charArr:
        if len(item) <= 5:
            char_pos = -1
        for special_char in ['░', '█', '▀']:
            char_pos = item.find(special_char)
            if char_pos != -1:
                break
        
        if char_pos != -1:
                x = int(item[:char_pos])
                char = item[char_pos]
                y = int(item[char_pos+1:])
                char_positions[(x, y)] = char
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    print('Char pos', char_positions)

    print(f"\nNumber of characters found: {len(char_positions)}")
    print(f"Grid size: {max_x + 1} x {max_y + 1}")
    print("Characters:")
    for (x, y), char in char_positions.items():
        print(f"  {char} at ({x}, {y})")

    # Create and print the grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    for (x, y), char in char_positions.items():
        grid[max_y - y][x] = char

    print("\nDecoded message:")
    for row in grid:  # Print rows in the correct order
        print(''.join(row))

# Usage
url1 = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url2 = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"

decode_secret_message(url1)
decode_secret_message(url2)