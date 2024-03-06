import requests
from bs4 import BeautifulSoup


def fetch_wikipedia_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', {'id': 'mw-content-text'})
        if content:
            text = content.get_text()
            return text
        else:
            return "Unable to find content on the page."
    except requests.exceptions.RequestException as e:
        return f"{e}"


def main():
    wikipedia_url = input("Enter the Wikipedia URL: ")
    content = fetch_wikipedia_content(wikipedia_url)
    print(content)


if __name__ == "__main__":
    main()
