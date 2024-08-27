#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import requests
from bs4 import BeautifulSoup
import os
from concurrent.futures import ThreadPoolExecutor

cookies = {
    '__cflb': '02DiuD8AhNjcPpJkAnGMbKZD2YdMYosRsQPhzqeNYhTX2',
    'wpmanga-adult': '1',
    'PHPSESSID': '3o4vgrsjcisoofiv8rhpfeap18',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.manhwatoon.com',
    'priority': 'u=1, i',
    'referer': 'https://www.manhwatoon.com/manga/re-monarch/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

image_headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'i',
    'referer': 'https://www.manhwatoon.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

def download_image(url, i, save_dir, chapter_number):
    response = requests.get(url, headers=image_headers)
    if response.status_code == 200:
        filename = f"page_{i}.jpg"
        filepath = os.path.join(save_dir, filename)
        with open(filepath, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {chapter_number} - {filename}")
    else:
        print(f"Failed to download image {i} from {url}")

def process_chapter(link, session, desktop_path):
    chap = session.get(link)
    chap_soup = BeautifulSoup(chap.content, 'html.parser')
    chapter_title = chap_soup.find('h1', {'id': 'chapter-heading'}).text.strip()
    chapter_images = chap_soup.find_all('div', {'class': 'page-break no-gaps'})
    image_urls = [img['data-src'].strip() for div in chapter_images for img in div.find_all('img') if 'data-src' in img.attrs]

    manga_name = chapter_title.split('-')[0].strip()
    manga_name = re.sub(r'[<>:"/\\|?*]', '', manga_name)
    chapter_number = chapter_title.split('-')[1].strip()
    chapter_number = re.sub(r'[<>:"/\\|?*]', '', chapter_number)

    save_dir = os.path.join(desktop_path, manga_name, chapter_number)
    os.makedirs(save_dir, exist_ok=True)

    # Download images concurrently
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i, url in enumerate(image_urls, start=1):
            executor.submit(download_image, url, i, save_dir, chapter_number)

    print(f"All downloads complete for {chapter_number}.")

def main():
    manga = str(input("Enter the URL of the Manga: "))
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    with requests.Session() as session:
        session.cookies.update(cookies)
        session.headers.update(headers)
        response = session.post(manga + 'ajax/chapters/')

        soup = BeautifulSoup(response.content, "html.parser")
        all_chapters = soup.find_all('a', href=True)

        links = {a['href'] for a in all_chapters if not a['href'].startswith("#")}
        links = list(links)
        for link in links:
            process_chapter(link, session, desktop_path)

if __name__ == "__main__":
    main()

