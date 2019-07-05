#!/usr/bin/python
import requests
import sqlite3
from bs4 import BeautifulSoup as bs

from music_styles import Music_style as ms


__ROOT_LINK = 'https://www.cifraclub.com.br/'

# returns the html from this url
def get_page_content(url):
    page = requests.get(url, timeout=5)
    return bs(page.content, "html.parser")  # parse the url content


# Tries to find js-sng_list at this url
def get_best_music_list(url):
    page_content = get_page_content(url)
    if page_content:
        song_list = page_content.find(id="js-sng_list")  # find the song list
        # Find all href inside a song list
        all_links_songs = [a['href'] for a in song_list.find_all('a', href=True) if a.text]

        music_style = url.split("/")[-1]  # get only the style from url
        return music_style, all_links_songs


def main():
    # letters = string.ascii_lowercase  # all the letters from 'a' to 'z'
    links = map(get_best_music_list, ["{}mais-acessadas/{}".format(__ROOT_LINK, style.value) for style in ms])


if __name__ == "__main__":
    main()
