import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = set()

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and urlparse(href).netloc == domain and '#' not in href:
            full_url = urljoin(url, href)
            links.add(full_url)

    return links


def save_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_text = soup.get_text()

    domain = urlparse(url).netloc
    with open(f'{domain}.txt', 'a', encoding='utf-8') as file:
        file.write(f"\n\n--- {url} ---\n\n")
        file.write(page_text)
    print(f"{url} の内容が {domain}.txt に追記されました。")


crawled_urls = set()


def crawl(url):
    if url not in crawled_urls:
        crawled_urls.add(url)
        save_content(url)

        links = get_links(url)
        for link in links:
            crawl(link)


def crawl_start(url):
    crawl("https://" + url)
