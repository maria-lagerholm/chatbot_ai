import requests
from bs4 import BeautifulSoup
import os

def get_child_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    child_links = [link.get('href') for link in soup.find_all('a') if link.get('href') and link.get('href').startswith('http')]
    return child_links

def save_to_txt(content, filename):
    with open(filename, 'a') as file:
        file.write(content + '\n')

def main():
    base_url = "https://www.allabolag.se/5569418576/byggok-ab"
    child_links = get_child_links(base_url)

    if not os.path.exists('scraped_data'):
        os.makedirs('scraped_data')

    save_to_txt(requests.get(base_url).text, 'scraped_data/main_page.txt')

    for idx, link in enumerate(child_links):
        try:
            content = requests.get(link).text
            save_to_txt(content, f'scraped_data/child_page_{idx}.txt')
        except Exception as e:
            print(f"Failed to fetch {link}: {e}")

if __name__ == "__main__":
    main()
