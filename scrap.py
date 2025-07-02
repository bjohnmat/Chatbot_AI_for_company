
# %%
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

CACHE_FILE = "Site_content.txt"
BASE_URL = os.getenv("URL") # à adapter

# Récupère tous les liens internes
def get_internal_links(base_url):
    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = set()
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            full_url = urljoin(base_url, href)
            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                links.add(full_url)

        return list(links)

    except Exception as e:
        print(f"Erreur lors de l'extraction des liens : {e}")
        return []

# Scrape tout le site
def scrape_site(links):
    content = ""
    for url in links:
        try:
            print(f"Scraping {url}")
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            text = ' '.join(soup.stripped_strings)
            content += f"\n\n----- {url} -----\n{text}"
        except Exception as e:
            print(f"Erreur scraping {url} : {e}")
    return content

# Charge ou génère le contenu du site
def load_or_scrape_site(force_refresh=False):
    if not force_refresh and os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return f.read()

    links = get_internal_links(BASE_URL)
    full_content = scrape_site(links)

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        f.write(full_content)

    return full_content
