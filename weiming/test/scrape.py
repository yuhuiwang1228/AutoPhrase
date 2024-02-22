import requests
from bs4 import BeautifulSoup

def check_phrase(phrase):
    formatted_phrase = phrase.replace(' ', '+')
    url = f"https://dictionary.cambridge.org/search/english/direct/?q={formatted_phrase}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            entry = soup.find('div', class_='pr entry-body__el')
            if entry:
                # print(f"The phrase '{phrase}' exists in the Cambridge Dictionary.")
                return True
            else:
                # print(f"The phrase '{phrase}' does not exist in the Cambridge Dictionary.")
                return False

        elif response.status_code not in range(200, 400): # nancy
            raise IndeedException(f"bad response with status code: {response.status_code}")

        else:
            print("Failed to retrieve information from Cambridge Dictionary.")

    except Exception as e:
        raise IndeedException(str(e))

# Example usage
# phrase = "eee eee eee"
# check_phrase(phrase)
