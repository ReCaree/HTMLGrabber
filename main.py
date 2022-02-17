import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time
init(autoreset=True)

first_launch = False

if first_launch == True:
    with open('main.py', 'r', encoding='utf-8') as txt:
        text = txt.readlines()
        text[9] = 'first_launch = False\n'

        with open('main.py', 'w', encoding='utf-8') as txt:
            txt.writelines(text)

            path = os.path.join('.', 'Website')
            os.mkdir(path, 0o666)
            print(f'{Fore.LIGHTGREEN_EX}Website folder created!')

def isValidUrl(url):
    if url.startswith('http://') or url.startswith('https://'):
        return True
    else:
        return False

def main():
    try:
        try:
            try:
                try:
                    r = requests.get(sys.argv[1]).content
                    soup = BeautifulSoup(r, 'html.parser')

                    for title in soup.find_all('title'):
                        with open(f'website/{title.get_text()}.html', 'w', encoding='utf-8') as f:
                            f.write(soup.prettify())

                    # print done message with light green color
                    print(Fore.LIGHTGREEN_EX + 'Done!')
                except requests.exceptions.SSLError:
                    print(Fore.LIGHTRED_EX + '⚠️  Danger: SSL Certificate error!')
                    print(Fore.YELLOW + 'Making Request Without Using Certificates...')
                    time.sleep(1)

                    r = requests.get(sys.argv[1], verify=False).content
                    soup = BeautifulSoup(r, 'html.parser')

                    for title in soup.find_all('title'):
                        with open(f'website/{title.get_text()}.html', 'w', encoding='utf-8') as f:
                            f.write(soup.prettify())
                    # print done message with light green colo  r
                    print(Fore.LIGHTGREEN_EX + 'Done!')
            except IndexError:
                print(Fore.LIGHTRED_EX + 'Please enter a URL')

        except requests.exceptions.ConnectionError:
            print(Fore.LIGHTRED_EX + 'Please enter a valid URL')
    except requests.exceptions.MissingSchema:
        if isValidUrl(sys.argv[1]) == True:
            os.system('python main.py ' + sys.argv[1])
        elif isValidUrl(sys.argv[1]) == False:
            os.system('python main.py https://' + sys.argv[1])
            

main()