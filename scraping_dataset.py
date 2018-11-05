#!/usr/bin/python
from bs4 import BeautifulSoup as bs
import requests
import string


def get_page_content(link):
    page = requests.get(link, timeout=5)
    return bs(page.content, "html.parser")  # parse the url content


def main():
    root_link = 'https://www.catho.com.br/profissoes/cargo/'
    letters = string.ascii_lowercase  # all the letters from 'a' to 'z'

    for letter in letters:
        page_content = get_page_content('{}'.format(letter))



if __name__ == "__main__":
    main()